# Consensus and Profile in Python

Implementation of the
[Rosalind Consensus and Profile](https://rosalind.info/problems/cons/) problem.

It works on Linux, Macos, Windows (WSL is recommended), and in general on any
platform with Python3 support.

## Installation

```console
git clone https://github.com/alexpilotti/bix.git
cd bix/consensus_and_pwm

# Optional: use a Python environment
python3 -m venv .venv
. .venv/bin/activate

pip install -r requirements.txt
```

## Usage

Display the command line usage:

```console
./consensus.sh --help
usage: cli.py [-h] -f FASTA [--bgp-a BGP_A] [--bgp-c BGP_C] [--bgp-g BGP_G] [--bgp-t BGP_T]

Consensus and Profile

options:
  -h, --help            show this help message and exit
  -f FASTA, --fasta FASTA
                        <Required> Multiple DNA sequences in fasta format
  --bgp-a BGP_A         backgroup probability for base A, default is 0.25
  --bgp-c BGP_C         backgroup probability for base C, default is 0.25
  --bgp-g BGP_G         backgroup probability for base G, default is 0.25
  --bgp-t BGP_T         backgroup probability for base T, default is 0.25
```

Usage example, with a FASTA file located in the `samples` directory:

```console
./consensus.sh -f samples/consensus_test.fasta
Sequences:

Rosalind_1
ATCCAGCT
Rosalind_2
GGGCAACT
Rosalind_3
ATGGATCT
Rosalind_4
AAGCAACC
Rosalind_5
TTGGAACT
Rosalind_6
ATGCCATT
Rosalind_7
ATGGCACT

PFM:
A [[5. 1. 0. 0. 5. 5. 0. 0.]
C  [0. 0. 1. 4. 2. 0. 6. 1.]
G  [1. 1. 6. 3. 0. 1. 0. 0.]
T  [1. 5. 0. 0. 0. 1. 1. 6.]]

Consensus PFM:
ATGCAACT

PWM:
A [[ 1.51 -0.81  -inf  -inf  1.51  1.51  -inf  -inf]
C  [ -inf  -inf -0.81  1.19  0.19  -inf  1.78 -0.81]
G  [-0.81 -0.81  1.78  0.78  -inf -0.81  -inf  -inf]
T  [-0.81  1.51  -inf  -inf  -inf -0.81 -0.81  1.78]]

Consensus PWM:
ATGCAACT
```
