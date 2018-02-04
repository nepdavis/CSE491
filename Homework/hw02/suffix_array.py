import time


def next_p(pattern):

    alphabet = {"A": "C", "C": "G", "G": "T", "T": "TA"}

    return pattern[:-1] + alphabet[pattern[-1]]


def binary_search(array, pattern):

    left = 0
    c = len(array) // 2
    right = len(array) - 1

    while array[left] < pattern < array[right]:

        if pattern < array[c]:

            if c == (left + 1):

                return c

            right = c
            c = (left + right) // 2
            continue

        else:

            if c == (right - 1):

                return right

            left = c
            c = (left + right) // 2
            continue


def suffix_array(text):

    text += "$"

    array = [text[i:] for i in range(len(text))]

    array = sorted(array)

    return array


def main():

    files = input().split()

    # Opens the text file and pattern file (text file comes first)
    pattern = (open(files[0]).readline()).strip()
    text = (open(files[1]).readline()).strip()

    pre_build_time = time.time()

    s_array = suffix_array(text)

    print(s_array)

    print("Suffix array build time was {:.6f} seconds".
          format(time.time() - pre_build_time))

    first_pos = binary_search(s_array, pattern)

    second_pos = binary_search(s_array, next_p(pattern))

    print(first_pos, second_pos)


if __name__ == "__main__":

    main()
