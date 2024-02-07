import numpy as np

FASTA_START_SYMBOL = ">"
BASES = ["A", "C", "G", "T"]
DEFAULT_BGP = 0.25


def load_multi_fasta(path):
    sequences = []

    with open(path, "r") as f:
        desc = f.readline().strip()
        if not desc.startswith(FASTA_START_SYMBOL):
            raise Exception(
                'Invalid FASTA format. The first line must start with "%s"' %
                FASTA_START_SYMBOL)
        desc = desc[1:]

        seq = ""
        for line in f:
            seq_line = line.strip()
            if seq_line.startswith(FASTA_START_SYMBOL):
                sequences.append((desc, seq))
                seq = ""
                desc = seq_line[1:]
            else:
                seq += seq_line
        sequences.append((desc, seq))
    return sequences


def get_consensus_seq(m):
    consensus_seq = ""
    for i in range(0, m.shape[1]):
        max_val = 0
        max_base = None
        for j, base in enumerate(BASES):
            if m[j][i] > max_val:
                max_base = base
                max_val = m[j][i]
        consensus_seq += max_base
    return consensus_seq


def compute_matrices(sequences, bgps):
    if sum(bgps.values()) != 1:
        raise Exception(
            "The sum of the background probabilities for all the bases "
            "must be 1")

    _, seq = sequences[0]
    seq_len = len(seq)

    pfm = np.zeros([len(BASES), seq_len])
    for _, seq in sequences:
        for i, base in enumerate(seq):
            pfm[BASES.index(base)][i] += 1

    n = len(sequences)
    bps = np.array([bgps[base] for base in BASES])
    ppm = pfm / n
    # Ignore divide by zero errors in log2
    with np.errstate(divide='ignore'):
        pwm = np.log2(ppm / bps[:, None])

    return pfm, pwm
