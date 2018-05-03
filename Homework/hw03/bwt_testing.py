import sys
import time


class BWT:

    def __init__(self, text, pattern, suffix_array):

        self.t = text
        self.p = pattern
        self.suffix_array = suffix_array

        self.bw = []
        self.first = None
        self.last = None

    def run(self):

        """
        Main class run
        :return: Returns string for printing of matches and match locs
        """

        self.bwt()

        bwt_output = "BWT: " + " ".join([str(i) for i in self.last[:5]]) + \
                     " ... " + " ".join([str(i) for i in self.last[-5:]]) \
                     + "\n"

        print(bwt_output)

        start_pos, end_pos = self.backward_search()

        occ_output = "OCC: " + \
                     " ".join([str(self.occ("$", i)) for i in range(1, 6)]) +\
                     " ... " +\
                     " ".join([str(self.occ("T", i)) for i in range(-4, 0)] +
                              [str(self.occ("T", None))]) \
                     + "\n"

        print(occ_output)

        if start_pos is None:

            return "Total: 0"

        matches = end_pos - start_pos + 1

        locs = sorted([self.suffix_array[i] for i in range(start_pos,
                                                           end_pos + 1)])

        return "Total: " + str(matches) + ":  " \
               + " ".join([str(i) for i in locs])

    def occ(self, char, q):

        """
        OCC structure for backward search
        :param char: character
        :param q: index for prefix
        :return: number of matches
        """

        return sum([char == i for i in self.last[:q]])

    def backward_search(self):

        """
        Backward search for bwt
        :return: Start and end indices
        """

        big_c = {c: sum([i < c for i in self.last]) for c in ["A", "C", "G",
                                                              "T", "$"]}

        print("C:", big_c, "\n")

        i = len(self.p) - 1

        c = self.p[-1]

        start = big_c[c] + self.occ(c, 0) + 1

        end = big_c[c] + self.occ(c, len(self.suffix_array))

        while (start <= end) and (i >= 1):

            c = self.p[i - 1]

            start = big_c[c] + self.occ(c, start - 1) + 1

            end = big_c[c] + self.occ(c, end)

            i -= 1

        if end < start:

            return None, None

        else:

            return start - 1, end - 1

    def bwt(self):

        """
        The function takes a text array and a sorted suffix array and
        returns the BW transformed array of suffix permutations
        :return: bw object of permutations
        """

        for i in self.suffix_array:

            if i == 0:

                self.bw.append("$")

            else:

                self.bw.append(self.t[i - 1])

        self.first = "".join([i[0] for i in self.bw])
        self.last = "".join([i[-1] for i in self.bw])


def main():

    # store list of files
    files = sys.argv[1:]

    # Opens the text file and pattern file (text file comes first)
    pattern = (open(files[0]).readline()).strip()
    text = (open(files[1]).readline()).strip()
    suffix_array_file = (open(files[2]))

    suffix_array = [int(i) for i in suffix_array_file.readline().split()]

    start_time = time.time()

    transform = BWT(text, pattern, suffix_array)

    message = transform.run()

    end_time = time.time() - start_time

    print(message)

    runtime_str = "The runtime of this program was {:5f} " \
                  "seconds".format(end_time)

    runtime_file = open("runtime.txt", "w")

    runtime_file.write(runtime_str)

    runtime_file.close()


if __name__ == "__main__":

    main()
