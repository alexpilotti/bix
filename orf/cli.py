import argparse

import orf


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Open Reading Frames (ORF)')
    parser.add_argument('-f', '--fasta', action='store',
                        help='<Required> DNA sequence in fasta format',
                        required=True)
    parser.add_argument('-r', '--include-reverse_strand', action='store_true',
                        help='Look for ORFs in the reverse strand as well')
    results = parser.parse_args()

    return {"fasta": results.fasta,
            "include_reverse_strand": results.include_reverse_strand}


def _print_orfs(dna_seq):
    orfs = orf.find_orfs(dna_seq)
    print("")
    print("Open Reading Frames:")
    print("")
    for o in orfs:
        print(orf.translate(o))


def main():
    args = _parse_args()

    (desc, dna_seq) = orf.load_fasta(args["fasta"])
    print("DNA sequence description: %s" % desc)
    print("DNA sequence: %s" % dna_seq)
    _print_orfs(dna_seq)

    if args["include_reverse_strand"]:
        dna_reverse_seq = orf.get_reverse_strand_sequence(dna_seq)
        print("")
        print("Reverse complement DNA sequence: %s" % dna_reverse_seq)
        _print_orfs(dna_reverse_seq)


if __name__ == '__main__':
    main()
