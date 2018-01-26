import time


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

        while k >= 0 and i < m - 1 and p[k] != p[i]:

            if k == 0:

                pi[i] = 0
                break

            else:

                k = pi[k - 1]

        if p[k] == p[i]:

            k += 1

            pi[i] = k


def kmp(t, p):

    n = len(t)
    m = len(p)

    total = 0

    positions = []

    pi = [0 for _ in range(m)]

    k = 0

    pi_array(pi, m, p)

    for i in range(n):

        while k >= 0 and p[k] != t[i]:

            if k == 0:

                break

            else:

                k = pi[k - 1]

        if p[k] == t[i]:

            k += 1

        if k == m:

            total += 1

            positions.append(str(i - k + 1))

            k = pi[k - 1]

    pi = [str(i) for i in pi]

    result = "Pi is: " + " ".join(pi) + "\n" + "Total: " + str(total) +  \
             "  " + " ".join(positions)

    return result


def main():

    t_ = ((open("T3.txt", "r")).readline()).strip()
    p_ = ((open("P3.txt", "r")).readline()).strip()

    out = naive(t_, p_)
    out_ = kmp(t_, p_)

    print(out)
    print(out_)

    # # Gets file inputs (both on same line)
    # files = input().split()
    #
    # # Opens the text file and pattern file (text file comes first)
    # t_ = (open(files[0]).readline()).strip()
    # p_ = (open(files[1]).readline()).strip()
    #
    # prev_time = time.time()
    #
    # # calls kmp() method and stores in out
    # out = kmp(t_, p_)
    #
    # new_time = time.time()
    #
    # # prints the kmp() return
    # print(out)
    # print("Total time elapsed:", round(new_time - prev_time, 10))

if __name__ == "__main__":

    main()
