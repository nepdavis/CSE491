import time


def pi_array(pi, m, p):

    """
    This function pre-processes the auxiliary array pi for the kmp algorithm
    :param pi: Original pi array of m 0's
    :param m: length of pattern string p
    :param p: pattern string
    :return: None (augments pi array in place)
    """

    # init counter at 0
    k = 0

    # for pi element from 1 to length of pattern m - 1
    for i in range(1, m):

        # while k >= 0 and kth pattern element not equal to ith pattern element
        while k >= 0 and p[k] != p[i]:

            # if k is 0
            if k == 0:

                # the ith element of pi is 0
                pi[i] = 0

                # continue to next i
                break

            # if k > 0
            else:

                # k now equal to k - 1 element of pi
                k = pi[k - 1]

        # if kth element of pattern same as ith element of pattern
        if p[k] == p[i]:

            # increment k by one
            k += 1

            # ith element of pi is now equal to k
            pi[i] = k


def kmp(t, p):

    # init n, m as length of text t and pattern p, respectively
    n = len(t)
    m = len(p)

    # init total pattern matches at 0
    total = 0

    # init empty list of matched pattern locations
    positions = []

    # init auxiliary array pi of m number of 0's
    pi = [0 for _ in range(m)]

    # init counter at 0
    k = 0

    # pre-process the auxiliary array pi (happens in place)
    pi_array(pi, m, p)

    # for each index of char in string text t
    for i in range(n):

        # while counter non-negative and pattern char and text char not same
        while k >= 0 and p[k] != t[i]:

            # if counter is 0
            if k == 0:

                # iterate to next text t index
                break

            # if counter k is > 0
            else:

                # then k now equal to k - 1 element of pi
                k = pi[k - 1]

        # if pattern char at k and current text char same
        if p[k] == t[i]:

            # increment k by one
            k += 1

        # if k is length of pattern
        if k == m:

            # pattern matches substring of t, increment matches by one
            total += 1

            # add location of match to list
            positions.append(str(i - k + 1))

            # k now equal to k - 1 element of auxiliary array pi
            k = pi[k - 1]

    # convert pi to list of strings for printing
    pi = [str(i) for i in pi]

    # create string output that is pi array and total number of matches
    # and those match locations
    result = "Pi is: " + " ".join(pi) + "\n" + "Total: " + str(total) +  \
             "  " + " ".join(positions)

    return result


def main():

    """
    This function asks user for files text and pattern. It then runs kmp
    algorithm using kmp(). It reports the kmp() output of matches and their
    locations. Also prints out running time of algorithm
    :return: None
    """

    # Gets file inputs (both on same line)
    files = input().split()

    # Opens the text file and pattern file (text file comes first)
    p_ = (open(files[0]).readline()).strip()
    t_ = (open(files[1]).readline()).strip()

    # save current time
    prev_time = time.time()

    # calls kmp() method and stores in out
    out = kmp(t_, p_)

    # save new time after algorithm run
    new_time = time.time()

    # prints the kmp() return
    print(out)

    # prints time elapsed from algorithm run
    print("Total time elapsed:", round(new_time - prev_time, 10))


if __name__ == "__main__":

    main()
