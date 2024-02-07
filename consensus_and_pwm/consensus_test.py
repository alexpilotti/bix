import os

from Bio import motifs
from Bio import SeqIO

import consensus


def _get_consensus_seq(fasta_path):
    sequences = consensus.load_multi_fasta(fasta_path)
    bgps = {"A": consensus.DEFAULT_BGP, "C": consensus.DEFAULT_BGP,
            "G": consensus.DEFAULT_BGP, "T": consensus.DEFAULT_BGP}
    pfm, _ = consensus.compute_matrices(sequences, bgps)
    return pfm, consensus.get_consensus_seq(pfm)


def _get_biopython_consensus_seq(fasta_path):
    sequences = list(SeqIO.parse(fasta_path, "fasta"))
    m = motifs.create(sequences)
    return m.counts, m.consensus


def main():
    module_dir = os.path.dirname(__file__)
    fasta_path = os.path.join(module_dir, "./samples/consensus_test.fasta")

    pfm1, consensus1 = _get_consensus_seq(fasta_path)
    pfm2, consensus2 = _get_biopython_consensus_seq(fasta_path)

    for i, base in enumerate(consensus.BASES):
        assert pfm2[base] == pfm1[i].tolist()

    assert consensus1 == consensus2


if __name__ == '__main__':
    main()
