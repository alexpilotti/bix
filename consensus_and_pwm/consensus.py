FASTA_START_SYMBOL = ">"


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


def compute_consensus(sequences):
    _, seq = sequences[0]
    seq_len = len(seq)

    profile = {"A": [0] * seq_len,
               "T": [0] * seq_len,
               "C": [0] * seq_len,
               "G": [0] * seq_len}

    for _, seq in sequences:
        for i, base in enumerate(seq):
            profile[base][i] += 1

    consensus_seq = ""
    for i in range(0, seq_len):
        max_val = 0
        max_base = None
        for base in profile.keys():
            if profile[base][i] > max_val:
                max_base = base
                max_val = profile[base][i]
        consensus_seq += max_base

    return profile, consensus_seq
