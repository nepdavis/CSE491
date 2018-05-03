import sys
import time


class GlobalAlignment:

    def __init__(self, x, y, match, mismatch, gap):

        self.x = x
        self.y = y

        self.n = len(x)
        self.m = len(y)

        self.match = match
        self.mismatch = mismatch
        self.d = gap

        self.f = [[0] * (self.m + 1) for _ in range(self.n + 1)]

    def s(self, a, b):

        if a == b:

            return self.match

        return self.mismatch

    def fill_table(self):

        for i in range(self.n + 1):

            self.f[i][0] = i * self.d

        for j in range(self.m + 1):

            self.f[0][j] = j * self.d

        for i in range(1, self.m + 1):

            for j in range(1, self.n + 1):

                self.f[i][j] = max(self.f[i - 1][j - 1] +
                                   self.s(self.x[i - 1], self.y[j - 1]),
                                   self.f[i - 1][j] + self.d,
                                   self.f[i][j - 1] + self.d)

        return self.f


def main():

    # Opens the text file and pattern file (text file comes first)
    text_x = (open(sys.argv[1]).readline()).strip()
    text_y = (open(sys.argv[2]).readline()).strip()

    match_score = sys.argv[3]
    mismatch_score = sys.argv[4]
    gap_score = sys.argv[5]

    start_time = time.time()

    result = GlobalAlignment(text_x, text_y, match_score, mismatch_score,
                             gap_score)

    running_time = time.time() - start_time

    print(result, "Total running time was:", running_time)


if __name__ == "__main__":

    main()
