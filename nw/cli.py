import argparse

import nw


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Needleman-Wunsch algorithm')
    parser.add_argument('-f1', '--fasta1', action='store',
                        help='<Required> First sequence in fasta format',
                        required=True)
    parser.add_argument('-f2', '--fasta2', action='store',
                        help='<Required> Second sequence in fasta format',
                        required=True)
    parser.add_argument('-b', '--blosum', action='store',
                        help='<Required> BLOSUM matrix',
                        required=True)
    parser.add_argument('-p', '--gap-penalty', action='store', type=int,
                        help='<Required> Gap penalty, e.g. -8',
                        required=True)
    parser.add_argument('--print-matrix', action='store_true',
                        help='Print the synamic programming matrix')
    results = parser.parse_args()

    return {"fasta1": results.fasta1,
            "fasta2": results.fasta2,
            "blosum": results.blosum,
            "gap_penalty": results.gap_penalty,
            "print_matrix": results.print_matrix}


def _print_matrix(m):
    print(m)
    print("")


def _print_alignments(alignments, desc1, desc2):
    print("Sequence 1: %s" % desc1)
    print("Sequence 2: %s" % desc2)
    print("")

    for al1, al2 in alignments:
        print(al1)
        bars = ""
        for i, x in enumerate(al1):
            bars += ("|" if al2[i] == x else " ")
        print(bars)
        print(al2)
        print("")


def main():
    args = _parse_args()

    desc1, seq1 = nw.load_fasta(args["fasta1"])
    desc2, seq2 = nw.load_fasta(args["fasta2"])
    blosum = nw.load_blosum(args["blosum"])
    gap_penalty = args["gap_penalty"]

    m = nw.compute_matrix(seq1, seq2, blosum, gap_penalty)
    alignments = nw.find_alignments(m, seq1, seq2, blosum, gap_penalty)

    if args["print_matrix"]:
        _print_matrix(m)

    _print_alignments(alignments, desc1, desc2)


if __name__ == '__main__':
    main()
