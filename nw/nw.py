import json
import os

import numpy as np

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


def load_blosum(blosum):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "data", "%s.json" % blosum.lower())

    with open(path, "r") as f:
        return json.load(f)


def _s(s, x, y):
    return s[''.join(sorted((x, y)))]


def compute_matrix(s1, s2, s, d):
    m = np.zeros([len(s2) + 1, len(s1) + 1], dtype=np.int16)

    m[0][0] = 0
    for i in range(1, len(s1) + 1):
        m[0][i] = m[0][i-1] + d
    for i in range(1, len(s2) + 1):
        m[i][0] = m[i-1][0] + d

    for i, x in enumerate(s1, 1):
        for j, y in enumerate(s2, 1):
            f1 = m[j-1][i-1] + _s(s, x, y)
            f2 = m[j][i-1] + d
            f3 = m[j-1][i] + d
            m[j][i] = max(f1, f2, f3)

    return m


def _find_alignments(m, s1, s2, s, d, alignments, i, j, al1, al2):
    if i > 0 or j > 0:
        x = s1[i-1]
        y = s2[j-1]

        if i > 0 and j > 0 and m[j][i] == m[j-1][i-1] + _s(s, x, y):
            _find_alignments(m, s1, s2, s, d, alignments,
                             i-1, j-1, x + al1, y + al2)
        if i > 0 and m[j][i] == m[j][i-1] + d:
            _find_alignments(m, s1, s2, s, d, alignments,
                             i-1, j, x + al1, "-" + al2)
        if j > 0 and m[j][i] == m[j-1][i] + d:
            _find_alignments(m, s1, s2, s, d, alignments,
                             i, j-1, "-" + al1, y + al2)
    else:
        alignments.append((al1, al2))


def find_alignments(m, s1, s2, s, d):
    alignments = []
    i = len(s1)
    j = len(s2)

    _find_alignments(m, s1, s2, s, d, alignments, i, j, "", "")

    return alignments


def _create_blosum_json(txt_path, json_path):
    """Convert a Blosum matrix in txt file format to json
    """
    m = []
    with open(txt_path, "r") as f:
        line = f.readline()
        m.append([""] + line.split())
        for line in f:
            m.append(line.split())

    h = {}
    for i in range(1, len(m) - 1):
        for j in range(1, i+1):
            h[''.join(sorted((m[0][i] + m[j][0]).upper()))] = int(m[i][j])

    with open(json_path, "w") as f:
        json.dump(h, f, sort_keys=True, indent=4)
