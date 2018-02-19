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

        self.bwt()

        start_pos, end_pos = self.backward_search()

        if start_pos is None:

            return "Total: 0"

        matches = end_pos - start_pos + 1

        locs = sorted([self.suffix_array[i] for i in range(start_pos,
                                                           end_pos + 1)])

        return "Total: " + str(matches) + "  " \
               + " ".join([str(i) for i in locs])

    def occ(self, char, q):

        return sum([char == i for i in self.last[:q]])

    def backward_search(self):

        big_c = {c: sum([i < c for i in self.last]) for c in ["A", "C", "G",
                                                              "T", "$"]}

        i = len(self.p) - 1

        c = self.p[i]

        start = big_c[c] + 1

        end = big_c[sorted(big_c.keys())[sorted(big_c.keys()).index(c) + 1]]

        while (start < end) and (i >= 1):

            c = self.p[i - 1]

            start = big_c[c] + self.occ(c, start - 1) + 1 - 1

            end = big_c[c] + self.occ(c, end) - 1

            i -= 1

        if end < start:

            return None, None

        else:

            return start, end

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

    suffix_array = None

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
