import time


def binary_search(array, pattern):

    left = 0
    right = len(array)

    while array[left] < pattern < array[right]:

        c = (left + right) // 2

        if pattern < array[c]:

            if c == left + 1:

                return c

            right = c + 0
            continue

        elif pattern > array[c]:

            if c == right - 1:

                return c

            left = c + 0
            continue


def suffix_array(text):

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

    print("Suffix array build time was {:.6f} seconds".
          format(time.time() - pre_build_time))

    print(s_array)


if __name__ == "__main__":

    main()
