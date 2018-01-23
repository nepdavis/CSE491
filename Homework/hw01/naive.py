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

    t_ = ((open("T1.txt", "r")).readline()).strip()
    p_ = ((open("P1.txt", "r")).readline()).strip()

    out = naive(t_, p_)

    print(out)


if __name__ == "__main__":

    main()

