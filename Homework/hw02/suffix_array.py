import sys
import time


def quick_sort(array, l = 0):

    if len(array) <= 1:

        return array

    same = [s for s in array if len(s[0]) == l]

    pivot = array[0][0]

    less = [s for s in array if s[0][l] < pivot[l]]
    equal = [s for s in array if s[0][l] == pivot[l]]
    greater = [s for s in array if s[0][l] > pivot[l]]

    less = quick_sort(less, l)
    equal = quick_sort(equal, l + 1)
    greater = quick_sort(greater, l)

    return same + less + equal + greater


def next_p(pattern):

    alphabet = {"A": "C", "C": "G", "G": "T", "T": "T"}

    if pattern[-1] == "T":

        return alphabet[pattern[0]]

    return pattern[:-1] + alphabet[pattern[-1]]


def binary_search(t, array, pattern):

    left = 0
    c = len(array) // 2
    right = len(array) - 1

    while t[array[left]:] < pattern < t[array[right]:]:

        if pattern < t[array[c]:]:

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

    array = [(text[i:], i) for i in range(len(text))]

    array = [i[1] for i in quick_sort(array)]

    return array


def main():

    files = sys.argv[1:]

    # Opens the text file and pattern file (text file comes first)
    pattern = (open(files[0]).readline()).strip()
    text = (open(files[1]).readline()).strip() + "$"

    pre_build_time = time.time()

    s_array = suffix_array(text)

    print("End of suffix array building. The time is {:.6f}".
          format(time.time() - pre_build_time))

    first_pos = binary_search(text, s_array, pattern)

    second_pos = binary_search(text, s_array, next_p(pattern))

    match_pos = sorted([s_array[i] for i in range(first_pos, second_pos)])

    print("Matches found at positions:", "  ".join(str(i) for i in match_pos))


if __name__ == "__main__":

    main()
