# Open Reading Frames in Python

Implementation of the
[Rosalind Open Reading Frames](https://rosalind.info/problems/orf/) problem.

It works on Linux, Macos, Windows (WSL is recommended), and in general on any
platform with Python3 support.

## Installation

```console
git clone https://github.com/alexpilotti/bix.git
cd bix/orf

# Optional: use a Python environment
python3 -m venv .venv
. .venv/bin/activate

pip install -r requirements.txt
```

## Usage

Display the command line usage:

```console
./orf.sh --help
usage: cli.py [-h] -f FASTA [-r]

Open Reading Frames (ORF)

options:
  -h, --help            show this help message and exit
  -f FASTA, --fasta FASTA
                        <Required> DNA sequence in fasta format
  -r, --include-reverse_strand
                        Look for ORFs in the reverse strand as well
```

Usage example, with a FASTA file located in the `samples` directory:

```console
./orf.sh  -f ./samples/orfs_rosalind.fasta -r
DNA sequence description: Rosalind_99
DNA sequence: AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Open Reading Frames:

MGMTPRLGLESLLE
MTPRLGLESLLE
M

Reverse complement DNA sequence: CTGAGATGCTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTCTAATCCAAGTCGCGGGGTCATCCCCATGTAACCTGAGTTAGCTACATGGCT

Open Reading Frames:

M
MLLGSFRLIPKETLIQVAGSSPCNLS
```
