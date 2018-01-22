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


def pi_array(pi, m, p):

    k = 0

    for i in range(1, m):

        while k >= 0 and p[k + 1] != p[i]:

            if k == 0:

                pi[i] = 0

            else:

                k = pi[k - 1]

        k += 1

        pi[i] = k


def kmp(t, p):

    n = len(t)
    m = len(p)

    total = 0

    positions = []

    pi = [0 for _ in range(m)]

    k = 0

    print(pi)

    pi_array(pi, m, p)

    print(pi)

    for i in range(n):

        while k >= 0 and p[k] != t[i]:

            k = pi[k]

        k += 1

        if k == m:

            total += 1

            positions.append(str(i))

            k = pi[k - 1]

    pi = [str(i) for i in pi]

    result = "Pi is: " + " ".join(pi) + "\n" + "Total: " + str(total) +  \
             "  " + " ".join(positions)

    return result


def main():

    t_ = ((open("T1.txt", "r")).readline()).strip()
    p_ = ((open("P1.txt", "r")).readline()).strip()

    # out = naive(t_, p_)
    out = kmp(t_, p_)

    print(out)


if __name__ == "__main__":

    main()
