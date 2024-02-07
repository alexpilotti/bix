import argparse

import consensus


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Consensus and Profile')
    parser.add_argument('-f', '--fasta', action='store',
                        help='<Required> Multiple DNA sequences '
                        'in fasta format',
                        required=True)
    results = parser.parse_args()

    return {"fasta": results.fasta}


def main():
    args = _parse_args()

    sequences = consensus.load_multi_fasta(args["fasta"])
    pfm, consensus_seq = consensus.compute_consensus(sequences)

    print("Sequences:")
    print("")
    for desc, seq in sequences:
        print(desc)
        print(seq)

    print("")
    print("Consensus:")
    print(consensus_seq)
    print("")
    print("Profile:")
    for k, v in pfm.items():
        print("%s: %s" % (k, v))


if __name__ == '__main__':
    main()
