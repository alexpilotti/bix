import argparse

import numpy as np

import consensus


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Consensus and Profile')
    parser.add_argument('-f', '--fasta', action='store',
                        help='<Required> Multiple DNA sequences '
                        'in fasta format',
                        required=True)
    parser.add_argument('--bgp-a', action='store',
                        help='backgroup probability for base A, '
                        'default is 0.25', default=consensus.DEFAULT_BGP)
    parser.add_argument('--bgp-c', action='store',
                        help='backgroup probability for base C, '
                        'default is 0.25', default=consensus.DEFAULT_BGP)
    parser.add_argument('--bgp-g', action='store',
                        help='backgroup probability for base G, '
                        'default is 0.25', default=consensus.DEFAULT_BGP)
    parser.add_argument('--bgp-t', action='store',
                        help='backgroup probability for base T, '
                        'default is 0.25', default=consensus.DEFAULT_BGP)
    results = parser.parse_args()

    return {"fasta": results.fasta,
            "bgp_a": results.bgp_a,
            "bgp_c": results.bgp_c,
            "bgp_g": results.bgp_g,
            "bgp_t": results.bgp_t}


def _print_matrix(m):
    s = np.array2string(m, precision=2).splitlines()
    for i, base in enumerate(consensus.BASES):
        print("%s %s" % (base, s[i]))


def main():
    args = _parse_args()

    sequences = consensus.load_multi_fasta(args["fasta"])
    bgps = {"A": args["bgp_a"], "C": args["bgp_c"],
            "G": args["bgp_g"], "T": args["bgp_t"]}
    pfm, pwm = consensus.compute_matrices(sequences, bgps)

    consensus_pfm = consensus.get_consensus_seq(pfm)
    consensus_pwm = consensus.get_consensus_seq(pwm)

    print("Sequences:")
    print("")
    for desc, seq in sequences:
        print(desc)
        print(seq)

    print("")
    print("PFM:")
    _print_matrix(pfm)
    print("")
    print("Consensus PFM:")
    print(consensus_pfm)

    print("")
    print("PWM:")
    _print_matrix(pwm)
    print("")
    print("Consensus PWM:")
    print(consensus_pwm)


if __name__ == '__main__':
    main()
