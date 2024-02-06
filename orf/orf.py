CODON_LENGHT = 3
START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]
GENETIC_CODE = {
      "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M", "ACA": "T", "ACC": "T",
      "ACG": "T", "ACT": "T", "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
      "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R", "CTA": "L", "CTC": "L",
      "CTG": "L", "CTT": "L", "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
      "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q", "CGA": "R", "CGC": "R",
      "CGG": "R", "CGT": "R", "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
      "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A", "GAC": "D", "GAT": "D",
      "GAA": "E", "GAG": "E", "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
      "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S", "TTC": "F", "TTT": "F",
      "TTA": "L", "TTG": "L", "TAC": "Y", "TAT": "Y", "TGC": "C", "TGT": "C",
      "TGG": "W"}
DNA_BASE_PAIRS = {"T": "A", "A": "T", "C": "G", "G": "C"}
FASTA_START_SYMBOL = ">"


def load_fasta(path):
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
            # Only the first sequence is loaded
            if seq_line.startswith(FASTA_START_SYMBOL):
                break
            seq += seq_line

    return desc, seq


def get_reverse_strand_sequence(seq):
    seq1 = ""
    for s in seq:
        seq1 += DNA_BASE_PAIRS[s]
    return seq1[::-1]


def find_orfs(seq):
    orfs = []
    i = seq.find(START_CODON)
    while i > 0:
        seq = seq[i:]
        codons = [(seq[i:i+CODON_LENGHT]).upper() for i in
                  range(0, len(seq), CODON_LENGHT)]

        current_orf = []
        for codon in codons:
            if current_orf and codon in STOP_CODONS:
                orfs.append(current_orf)
                current_orf = []
            elif current_orf or codon == START_CODON:
                current_orf.append(codon)

        i = seq.find(START_CODON, 1)
    return orfs


def translate(orf):
    seq = ""
    for codon in orf:
        seq += GENETIC_CODE[codon]
    return seq
