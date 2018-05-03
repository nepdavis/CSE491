import sys
import time


class GlobalAlignment:

    def __init__(self, x, y, match, mismatch, gap):

        self.x = x
        self.y = y

        self.n = len(x)
        self.m = len(y)

        self.match = int(match)
        self.mismatch = int(mismatch)
        self.d = int(gap)

    def scoring(self, align_x, align_y):

        score = 0

        for i, j in zip(align_x, align_y):

            if i == j:

                score += self.match

            elif i == "-" or j == "-":

                score += self.d

            else:

                score += self.mismatch

        return score

    def s(self, a, b):

        if a == b:

            return self.match

        return self.mismatch

    def fill_table(self, sub_x, sub_y):

        f_old = [j * self.d for j in range(len(sub_y) + 1)]

        f_new = []

        for i in range(1, len(sub_x) + 1):

            f_new = [i * self.d]

            for j in range(1, len(sub_y) + 1):

                f_new.append(max(f_old[j - 1] + self.s(sub_x[i - 1],
                                                       sub_y[j - 1]),
                                 f_old[j] + self.d, f_new[j - 1] + self.d))

            f_old = f_new[:]

        return f_new

    def nw_table(self, sub_x, sub_y):

        f = [[0] * (len(sub_y) + 1) for _ in range(len(sub_x) + 1)]

        for i in range(len(sub_x) + 1):

            f[i][0] = i * self.d

        for j in range(len(sub_y) + 1):

            f[0][j] = j * self.d

        for i in range(1, len(sub_x) + 1):

            for j in range(1, len(sub_y) + 1):

                f[i][j] = max(f[i - 1][j - 1] +
                              self.s(sub_x[i - 1], sub_y[j - 1]),
                              f[i - 1][j] + self.d, f[i][j - 1] + self.d)

        return f

    def nw(self, sub_x, sub_y):

        f = self.nw_table(sub_x, sub_y)

        x_align = ""
        y_align = ""

        i = len(sub_x)
        j = len(sub_y)

        while i > 0 or j > 0:

            if i > 0 and j > 0 and f[i][j] == (f[i - 1][j - 1] +
                                               self.s(sub_x[i-1], sub_y[j-1])):

                x_align += sub_x[i-1]
                y_align += sub_y[j-1]

                i -= 1
                j -= 1

            elif i > 0 and f[i][j] == (f[i-1][j] + self.d):

                x_align += sub_x[i-1]
                y_align += "-"

                i -= 1

            else:

                x_align += "-"
                y_align += sub_y[j-1]

                j -= 1

        return x_align[::-1], y_align[::-1]

    def hirsch(self, x = None, y = None):

        if x is None or y is None:

            x = self.x[:]
            y = self.y[:]

        z = ""
        w = ""

        if len(x) == 0:

            for i in range(len(y)):

                z += "-"
                w += y[i]

        elif len(y) == 0:

            for i in range(len(x)):

                z += x[i]
                w += "-"

        elif len(x) == 1 or len(y) == 1:

            z, w = self.nw(x, y)

        else:

            xmid = len(x) // 2

            score_l = self.fill_table(x[:xmid], y)

            score_r = self.fill_table((x[xmid:])[::-1], y[::-1])

            maxes = [sum([i, j]) for i, j in zip(score_l, score_r[::-1])]

            ymid = [i for i, j in enumerate(maxes) if j == max(maxes)][0]

            z_f, w_f = self.hirsch(x[:xmid], y[:ymid])

            z_s, w_s = self.hirsch(x[xmid:], y[ymid:])

            z = z_f + z_s
            w = w_f + w_s

        return z, w

    def run(self):

        alignments = self.hirsch()

        align_a, align_b = alignments[0], alignments[1]

        scoring = self.scoring(align_a, align_b)

        return str(scoring)


def main():

    # Opens the text file and pattern file (text file comes first)
    text_x = (open(sys.argv[1]).readline()).strip()
    text_y = (open(sys.argv[2]).readline()).strip()

    match_score = sys.argv[3]
    mismatch_score = sys.argv[4]
    gap_score = sys.argv[5]

    start_time = time.time()

    alg = GlobalAlignment(text_x, text_y, match_score, mismatch_score,
                          gap_score)

    result = alg.run()

    running_time = time.time() - start_time

    print("Optimal global alignment score:", result)
    print("Total running time: {:.6f} seconds".format(running_time))


if __name__ == "__main__":

    main()
