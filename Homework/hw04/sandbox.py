

def s(a, b):

    if a == b:

        return 1

    return -1


def fill_table(sub_x, sub_y):

    f_old = [j * -2 for j in range(len(sub_y) + 1)]

    f_new = []

    for i in range(1, len(sub_x) + 1):

        f_new = [i * -2]

        for j in range(1, len(sub_y) + 1):

            f_new.append(max(f_old[j - 1] +
                          s(sub_x[i - 1], sub_y[j - 1]),
                          f_old[j] + -2, f_new[j - 1] + -2))

        f_old = f_new[:]

    return f_new
