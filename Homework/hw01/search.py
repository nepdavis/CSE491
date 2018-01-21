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


def kmp(t, p):

    n = len(t)
    m = len(p)

    total = 0

    pi = [0 for _ in range(n)]

    k = 0

    for i in range(n):

        while k >= 0 and p[k + 1] != t[i]:

            k = pi[k]

        k += 1

        if k == m:

            total += 1

            k = pi[k]


t_ = ((open(input(""), "r")).readline()).strip()
p_ = ((open(input(""), "r")).readline()).strip()
