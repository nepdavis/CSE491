import sys


def parse_file(filename):

    all_series = []

    with open(filename) as f:

        for line in f:

            line = [int(i) for i in line.strip()]

            all_series.append(line)

    return all_series


def main():

    file = sys.argv[1]

    data = parse_file(file)


if __name__ == "__main__":

    main()
