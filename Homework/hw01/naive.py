import time


def naive(t, p):

    """
    Naive pattern matching algorithm that matches substring of T with P
    character by character from index 0 to n - m + 1
    :param t: a text string
    :param p: a pattern string
    :return: string result with total number of matches and their locations
    """

    # store lengths of t and p in n and m, respectively
    n = len(t)
    m = len(p)

    # init total matches at 0
    total = 0

    # init empty list keeping track of positions for matches
    positions = []

    # for each char in range of string t minus length of pattern plus 1
    for i in range(n - m + 1):

        # new string to compare is substring of t starting at i to i + m
        new = t[i:i+m]

        # init counter at 0
        j = 0

        # while j within m and new substring char equal to pattern char at jth
        while (j < m) and (new[j] == p[j]):

            # increment j
            j += 1

        # if, after while loop, j equal to m
        if j == m:

            # substring new must equal pattern, increment total by 1
            total += 1

            # add location i to positions as a string (for printing)
            positions.append(str(i))

    # formatted string result for printing
    result = "Total: " + str(total) + "  " + " ".join(positions)

    # return formatted string
    return result


def main():

    """
    This asks for an input of a text and pattern file/path and reads those
    files. It then calls the naive sorting algorithm and prints the return
    :return: 
    """

    # Gets file inputs (both on same line)
    files = input().split()

    # Opens the text file and pattern file (text file comes first)
    p_ = (open(files[0]).readline()).strip()
    t_ = (open(files[1]).readline()).strip()

    prev_time = time.time()

    # calls naive() method and stores in out
    out = naive(t_, p_)

    new_time = time.time()

    # prints the naive() return
    print(out)
    print("Total time elapsed:", round(new_time - prev_time, 10))


if __name__ == "__main__":

    # run main program
    main()
