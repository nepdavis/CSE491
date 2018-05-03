import sys


class OLC:

    def __init__(self, x, y, score, overlap):

        """
        Constructor for overlap alignment algorithm
        :param x: first sequence
        :param y: second sequence
        :param score: maximum score threshold
        :param overlap: minimum overlap threshold
        """

        self.x = x
        self.y = y

        self.m = len(x)
        self.n = len(y)

        self.min_score = score
        self.overlap = overlap

        self.score_table = {"A": {"A": 0, "C": 4, "G": 2, "T": 4, "-": 8},
                            "C": {"A": 4, "C": 0, "G": 4, "T": 2, "-": 8},
                            "G": {"A": 2, "C": 4, "G": 0, "T": 4, "-": 8},
                            "T": {"A": 4, "C": 2, "G": 4, "T": 0, "-": 8},
                            "-": {"A": 8, "C": 8, "G": 8, "T": 8}}

        self.table = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        self.x_align = ""
        self.y_align = ""

        self.found_alignment = True

        self.edges = 0

        self.matches = ""

    def score(self, a, b):

        """
        Returns the mismatch/match score between two characters
        :param a: first character
        :param b: second character
        :return: score for two characters from the hard-coded score table
        """

        return self.score_table[a][b]

    def fill_table(self):

        """
        Function to fill the table of scores between the two sequences
        :return: None
        """

        for i in range(1, self.n + 1):

            self.table[0][i] = 999999

        # init certain cells to infinity based on minimum overlap threshold
        if self.overlap > 0:

            for i in range(self.m, self.m + 1 - self.overlap, -1):

                self.table[i][0] = 999999

        for i in range(1, self.m):

            for j in range(1, self.n + 1):

                first = self.table[i - 1][j] + self.score(self.x[i - 1], "-")

                second = self.table[i][j - 1] + self.score("-", self.y[j - 1])

                third = self.table[i - 1][j - 1] + self.score(self.x[i - 1],
                                                              self.y[j - 1])

                self.table[i][j] = min(first, second, third)

        # fill last row based on overlap minimum number
        for j in range(self.n + 1):

            if j < self.overlap:

                self.table[-1][j] = 999999

            else:

                first = self.table[-1 - 1][j] + self.score(self.x[-1 - 1], "-")

                second = self.table[-1][j - 1] + self.score("-", self.y[j - 1])

                third = self.table[-1 - 1][j - 1] + self.score(self.x[-1 - 1],
                                                               self.y[j - 1])

                self.table[-1][j] = min(first, second, third)

    def traceback(self):

        """
        Traceback algorithm to get actual overlap alignment -- fills two
        strings
        :return: None
        """

        j = self.table[-1].index(min(self.table[-1]))

        i = self.m

        while j != 0:

            diag = self.table[i - 1][j - 1]

            upper = self.table[i - 1][j]

            left = self.table[i][j - 1]

            if upper <= diag and upper <= left:

                i -= 1

            elif diag <= left and diag <= upper:

                i -= 1
                j -= 1

            else:

                j -= 1

        self.y_align += " " * i
        self.y_align += self.y

        self.x_align += self.x
        self.x_align += " " * (len(self.y_align) - len(self.x))

    def total_score(self):

        """
        Gets total score for overlap alignment and checks whether this is
        greater than maximum score threshold
        :return: None
        """

        total = 0

        for i in range(len(self.x_align)):

            a = self.x_align[i]
            b = self.y_align[i]

            if a != " " and b != " ":

                total += self.score_table[a][b]

        if total > self.min_score:

            self.found_alignment = False

        if self.matches.count("|") < self.overlap:

            self.found_alignment = False

    def alignment(self):

        """
        Creates edges string to show actual overlap alignment
        :return: None
        """

        self.matches = ""

        for i in range(len(self.x_align)):

            if self.x_align[i] == self.y_align[i]:

                self.matches += "|"

                self.edges += 1

            else:

                self.matches += " "

    def output(self):

        """
        Constructs the overlap alignment for two sequences for output
        :return: Three line output of two sequences and their edges
        """

        return self.x_align + "\n" + self.matches + "\n" + self.y_align

    def run_all(self):

        """
        Runs entire algorithm together and fills all structures
        :return: None
        """

        self.fill_table()

        self.traceback()

        self.alignment()

        self.total_score()


def main():

    """
    Main function of program. Reads in all inputs and reads in .fa file using
    dictionary data structure to store sequences and their names
    :return: None (does print out number of overlap alignment edges)
    """

    file = sys.argv[1]

    length_threshold = int(sys.argv[2])
    cost_threshold = int(sys.argv[3])
    mask = int(sys.argv[4])

    all_lines = dict()

    temp = ""

    with open(file) as f:

        for line in f:

            if line[0] == ">":

                temp = line[1:].strip()

                continue

            else:

                all_lines[temp] = line.strip()

    edges_list = []
    mask_output_list = []

    for master_key in all_lines.keys():

        for temp_key in all_lines.keys():

            if master_key != temp_key:

                a = all_lines[master_key]
                b = all_lines[temp_key]

                alg = OLC(a, b, cost_threshold, length_threshold)

                alg.run_all()

                if alg.found_alignment is True:

                    edge = master_key + " " + temp_key + " " + str(alg.edges)

                    edges_list.append(edge)

                    if mask == 1:

                        mask_output_list.append(alg.output())

    for i in range(len(edges_list)):

        print(edges_list[i])

        if mask == 1:

            print(mask_output_list[i])


if __name__ == "__main__":

    main()
