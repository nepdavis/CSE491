import time


def bwt(t, suffix_array):

    """
    The function takes a text array and a sorted suffix array and returns the
    BW transformed array of suffix permutations
    :param t: text
    :param suffix_array: sorted suffix array of t
    :return: bw object of permutations
    """

    bw = []

    for i in suffix_array:

        if i == 0:

            bw.append("$")

        else:

            bw.append(t[i - 1])

    return bw


def main():

    start_time = time.time()

    end_time = time.time() - start_time

    runtime_str = "The runtime of this program was {:5f} " \
                  "seconds".format(end_time)

    runtime_file = open("runtime.txt", "w")

    runtime_file.write(runtime_str)

    runtime_file.close()


if __name__ == "__main__":

    main()
