import numpy as np
from matplotlib import colors
from matplotlib import pyplot as plt


def _create_mat(x, y):
    return np.zeros([y, x], dtype=bool)


def dotplot(seq_a, seq_b):
    x = len(seq_a)
    y = len(seq_b)

    m = _create_mat(x, y)
    for i, a in enumerate(seq_a):
        for j, b in enumerate(seq_b):
            if a == b:
                m[j][i] = 1
    return m


def print_dotplot_1(m):
    for i, row in enumerate(m):
        line = ""
        for x in row:
            line += "*" if x else " "
        print(line)


def print_dotplot_2(seq_a, seq_b, m):
    print("   %s" % seq_a)
    for i, row in enumerate(m):
        line = "%s |" % seq_b[i]
        for x in row:
            line += "*" if x else " "
        line += "|"
        print(line)


def print_dotplot_3(seq_a, seq_b, m):
    for i, row in enumerate(m):
        line = ""
        for x in row:
            line += seq_b[i] if x else " "
        print(line)


def show_dotplot_window(seq_a, seq_b, m):
    fig, ax = plt.subplots()
    ax.set_xticks(range(0, len(seq_a)))
    ax.set_xticklabels(seq_a)
    ax.set_yticks(range(0, len(seq_b)))
    ax.set_yticklabels(seq_b)

    w, h = m.shape
    ax.plot([0, h - 1], [0, w - 1], linestyle='solid', color="black")

    cmap = colors.ListedColormap(['white', 'black'])
    ax.imshow(m, cmap=cmap)

    plt.show()


def _print_separator():
    print("-" * 80)


def main():
    s1 = "DOROTHYCROWFOOTHODGKIN"
    s2 = "DOROTHYHODGKIN"

    m = dotplot(s1, s2)
    print_dotplot_1(m)
    _print_separator()

    print_dotplot_2(s1, s2, m)
    _print_separator()

    print_dotplot_3(s1, s2, m)
    _print_separator()

    show_dotplot_window(s1, s2, m)


if __name__ == '__main__':
    main()
