import time


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

    print("Suffix array build time was", time.time() - pre_build_time)

    print(s_array)


if __name__ == "__main__":

    main()
