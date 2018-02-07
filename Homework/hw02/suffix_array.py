import sys
import time


def quick_sort(array, l = 0):

    """
    Multi key quick sort for suffix array
    :param array: an unsorted suffix array
    :param l: a starting value for comparison index
    :return: a collection of partitioned lists
    """

    # if list has one element or empty
    if len(array) <= 1:

        # return sorted list
        return array

    # check to see if any strings empty
    same = [s for s in array if len(s[0]) == l]

    # choose first string as the pivot
    pivot = array[0][0]

    # define less, equal, and greater partitions
    less = [s for s in array if s[0][l] < pivot[l]]
    equal = [s for s in array if s[0][l] == pivot[l]]
    greater = [s for s in array if s[0][l] > pivot[l]]

    # begin recursion sorting and partitioning starting partitions
    less = quick_sort(less, l)
    equal = quick_sort(equal, l + 1)
    greater = quick_sort(greater, l)

    return same + less + equal + greater


def next_p(pattern):

    """
    Finds the following lexicographically pattern to input pattern
    :param pattern: pattern to increment lexicographically
    :return: the pattern that directly lexicographically follows the other
    pattern
    """

    # dictionary deciding next characters for new pattern
    alphabet = {"A": "C", "C": "G", "G": "T", "T": "T"}

    # if last character equal to last character in alphabet
    if pattern[-1] == "T":

        # if pattern also starts with T
        if pattern[0] == "T":

            # then return current pattern as there are none after it in text
            return pattern

        # return next character by itself
        return alphabet[pattern[0]]

    # return pattern with new ending character
    return pattern[:-1] + alphabet[pattern[-1]]


def binary_search(t, array, pattern):

    """
    Binary search algorithm for suffix array insert locations of pattern
    :param t: text collection to find matches in
    :param array: sorted suffix array
    :param pattern: pattern that you are finding matches for
    :return: most left location where you could insert pattern into suffix
    array
    """

    # initialize index variables for binary search
    left = 0
    c = len(array) // 2
    right = len(array) - 1

    # while pattern within correct bounds in suffix array
    while t[array[left]:] < pattern < t[array[right]:]:

        # if pattern left of center
        if pattern < t[array[c]:]:

            # if center next to left
            if c == (left + 1):

                # return c as the insert location
                return c

            # update indices and iterate
            right = c
            c = (left + right) // 2
            continue

        # if pattern right of center
        else:

            # if center next to right location
            if c == (right - 1):

                # return right index as insert location
                return right

            # if not then update indices and iterate
            left = c
            c = (left + right) // 2
            continue


def suffix_array(text):

    """
    Constructs suffix array
    :param text: text to create suffix array from (calls quick sort)
    :return: the sorted suffix array (indices only)
    """

    # get all suffixes from text, and their starting location
    array = [(text[i:], i) for i in range(len(text))]

    # create suffix array of sorted starting locations of suffixes, based on
    # suffix sorting from quick sort
    array = [i[1] for i in quick_sort(array)]

    # return sorted suffix array
    return array


def main():

    """
    Main run of program -- loads in text and pattern files. Constructs suffix
    array and then uses binary search to find number of matches and match
    locations
    :return: None
    """

    # store list of files
    files = sys.argv[1:]

    # Opens the text file and pattern file (text file comes first)
    pattern = (open(files[0]).readline()).strip()
    text = (open(files[1]).readline()).strip() + "$" # add dollar sign to end

    # init current time
    pre_build_time = time.time()

    # build sorted suffix array
    s_array = suffix_array(text)

    # print out time it took for suffix array construction
    print("End of suffix array building. The time is {:.6f}".
          format(time.time() - pre_build_time))

    # get first position of insertion from binary search
    first_pos = binary_search(text, s_array, pattern)

    # get position of insertion of next pattern from binary search
    second_pos = binary_search(text, s_array, next_p(pattern))

    # get suffix array locations from range of the two above locations
    match_pos = sorted([s_array[i] for i in range(first_pos, second_pos)])

    # print out sorted starting locations of matches found in text
    print("Matches found at positions:", "  ".join(str(i) for i in match_pos))


if __name__ == "__main__":

    main()
