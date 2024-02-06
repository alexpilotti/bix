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
usage: cli.py [-h] -f FASTA

Consensus and Profile

options:
  -h, --help            show this help message and exit
  -f FASTA, --fasta FASTA
                        <Required> Multiple DNA sequences in fasta format
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

Consensus:
ATGCAACT

Profile:
A: [5, 1, 0, 0, 5, 5, 0, 0]
T: [1, 5, 0, 0, 0, 1, 1, 6]
C: [0, 0, 1, 4, 2, 0, 6, 1]
G: [1, 1, 6, 3, 0, 1, 0, 0]
```
