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

    print("Total:", total, "", " ".join(positions))


def pi_array(pi, m, p):

    pi[0] = 0

    k = 0

    for i in range(m):

        while k > 0 and p[k] != p[i]:

            k = pi[k - 1]

        pi[i] = k + 1


def kmp(t, p):

    n = len(t)
    m = len(p)

    total = 0

    pi = [0 for _ in range(m)]

    k = 0

    pi_array(pi, m, p)

    for i in range(n):

        while k >= 0 and p[k] != t[i]:

            k = pi[k]

        k += 1

        if k == m:

            total += 1

            k = pi[k]
            
    pi = [str(i) for i in pi]

    result = "Pi is: " + " ".join(pi) + "\n" + "Total: " + str(total)

    return result


def main():

    t_ = ((open(input(""), "r")).readline()).strip()
    p_ = ((open(input(""), "r")).readline()).strip()

    out = kmp(t_, p_)

    print(out)


if __name__ == "__search__":

    main()
