# Needleman-Wunsch algorithm in Python

The `nw` directory contains an implementation of the Needleman-Wunsch algorith
to identify sequence alignments, written in Python, mostly for didactic usage.
Beside a primary Python module, a command line interface (CLI) for shell usage
is also included.

The `BLOSUM50` and `BLOSUM62` matrices are already included, more can be added
as needed, see the corresponding json files in the `data` directory.

It works on Linux, Macos, Windows (WSL is recommended), and in general on any
platform with Python3 support.

## Installation

```console
git clone https://github.com/alexpilotti/bix.git
cd bix/nw

# Optional: use a Python environment
python3 -m venv .venv
. .venv/bin/activate

pip install -r requirements.txt
```

## Usage

Display the comman line usage:

```console
./nw.sh --help
usage: cli.py [-h] -f1 FASTA1 -f2 FASTA2 -b BLOSUM -p GAP_PENALTY
              [--print-matrix]

Needleman-Wunsch algorithm

options:
  -h, --help            show this help message and exit
  -f1 FASTA1, --fasta1 FASTA1
                        <Required> First sequence in fasta format
  -f2 FASTA2, --fasta2 FASTA2
                        <Required> Second sequence in fasta format
  -b BLOSUM, --blosum BLOSUM
                        <Required> BLOSUM matrix
  -p GAP_PENALTY, --gap-penalty GAP_PENALTY
                        <Required> Gap penalty, e.g. -8
  --print-matrix        Print the synamic programming matrix
  ```

  Sample alignment, with the FASTA files located in the `samples` directory:

  ```console
  ./nw.sh -f1 ./samples/seq1.fasta -f2 ./samples/seq2.fasta -b blosum50 -p -8
Sequence 1: First sample sequence
Sequence 2: Second sample sequence

HEAGAWGHE-E
    || || |
--P-AW-HEAE

HEAGAWGHE-E
    || || |
-P--AW-HEAE

HEAGAWGHE-E
  |  | || |
-PA--W-HEAE
  ```

Display the dynamic programming matrix in the output:

```console
./nw.sh -f1 ./samples/seq1.fasta -f2 ./samples/seq2.fasta -b blosum50 -p -8 --print-matrix
[[  0  -8 -16 -24 -32 -40 -48 -56 -64 -72 -80]
 [ -8  -2  -9 -17 -25 -33 -41 -49 -57 -65 -73]
 [-16 -10  -3  -4 -12 -20 -28 -36 -44 -52 -60]
 [-24 -18 -11  -6  -7 -15  -5 -13 -21 -29 -37]
 [-32 -14 -18 -13  -8  -9 -13  -7  -3 -11 -19]
 [-40 -22  -8 -16 -16  -9 -12 -15  -7   3  -5]
 [-48 -30 -16  -3 -11 -11 -12 -12 -15  -5   2]
 [-56 -38 -24 -11  -6 -12 -14 -15 -12  -9   1]]

Sequence 1: First sample sequence
Sequence 2: Second sample sequence

HEAGAWGHE-E
    || || |
--P-AW-HEAE

HEAGAWGHE-E
    || || |
-P--AW-HEAE

HEAGAWGHE-E
  |  | || |
-PA--W-HEAE
```
