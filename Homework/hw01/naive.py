def naive(t, p):

    n = len(t)
    m = len(p)

    total = 0

    positions = []

    for i in range(n - m + 1):

        new = t[i:i+m]

        j = 0

        while (j < m) and (new[j] == p[j]):

            j += 1

        if j == m:

            total += 1
            positions.append(str(i))

    result = "Total: " + str(total) + "  " + " ".join(positions)

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
    t_ = (open(files[0]).readline()).strip()
    p_ = (open(files[1]).readline()).strip()

    # calls naive() method and stores in out
    out = naive(t_, p_)

    # prints the naive() return
    print(out)


if __name__ == "__main__":

    # run main program
    main()
