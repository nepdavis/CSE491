import sys
import numpy as np


def parse_file(filename):

    """
    Function to read in .fa file
    :param filename: .fa file
    :return: data as one string
    """

    data = ""

    with open(filename) as f:

        for line in f:

            if line.strip()[0] == ">":

                continue

            data += line.strip()

    return data.upper()


def read_params(filename):

    """
    Function to read in example.hmm parameters
    :param filename: example.hmm
    :return: parameters
    """

    lines = []

    with open(filename) as f:

        for line in f:

            lines.append(line.strip())

    # Parse first line

    num_states, num_emissions, emissions = lines[0].split()

    # num_states, num_emissions = int(num_states), int(num_emissions)

    emissions = [i for i in emissions]

    # Parse second line

    prob_a, prob_b = [float(i) for i in lines[1].split()]

    # Parse third line

    prob_table_a = {emissions[i]: float(lines[2].split()[2:][i]) for i in range(4)}

    prob_table_a["AA"], prob_table_a["AB"] = [float(i) for i in lines[2].split()[:2]]

    # Parse fourth line

    prob_table_b = {emissions[i]: float(lines[3].split()[2:][i]) for i in range(4)}

    prob_table_b["BA"], prob_table_b["BB"] = [float(i) for i in lines[3].split()[:2]]

    return prob_a, prob_b, prob_table_a, prob_table_b


def viterbi(data, prob_a, prob_b, a_probs, b_probs):

    """
    HMM and Viterbi algorithm for state transitions
    :param data: .fa as a string
    :param prob_a: init prob for a
    :param prob_b: init prob for b
    :param a_probs: a parameters
    :param b_probs: b parameters
    :return: state transitions
    """

    # transform to log space
    a_probs = {k: np.log(v) for k, v in a_probs.items()}
    b_probs = {k: np.log(v) for k, v in b_probs.items()}

    # init viterbi
    viterbi_a = [np.log(prob_a) + a_probs[data[0]]]
    viterbi_b = [np.log(prob_b) + b_probs[data[0]]]

    # create array for path state transitions
    path_states = np.zeros((2, len(data)), dtype = "int")

    # init path states
    path_states[1, 0] = 1

    # for each value in the .fa file
    for i in range(1, len(data)):

        a_options = [viterbi_a[i-1] + a_probs["AA"],
                     viterbi_b[i-1] + b_probs["BA"]]

        # max probability of a
        a = a_probs[data[i]] + max(a_options)

        # get path for new a
        path_states[0, i] = a_options.index(max(a_options))

        b_options = [viterbi_a[i-1] + a_probs["AB"],
                     viterbi_b[i-1] + b_probs["BB"]]

        # max probability for b
        b = b_probs[data[i]] + max(b_options)

        # get path for new b
        path_states[1, i] = b_options.index(max(b_options))

        viterbi_a.append(a)
        viterbi_b.append(b)

    # get state with max probability at end
    max_index = 0 if viterbi_a[-1] > viterbi_b[-1] else 1

    # initialize path
    path = [max_index]

    i = path[0]

    # tracing back, find optimal state for value given where it tranfered from
    for j in range(len(data)-2, -1, -1):

        i = path_states[i, j]

        path.append(i)

    # transform path to A and B (state names)
    path = ["A" if i == 0 else "B" for i in path]

    # return reversed path (correct order)
    return path[::-1]


def output(path, output_file):

    """
    Function to write algorithm output to file
    :param path: paths
    :param output_file: file name to write to
    :return: none
    """

    lines = []
    states = {"A": 0, "B": 0}
    current_line = "{:>10}".format(1)

    for i in range(1, len(path)):

        if path[i - 1] != path[i]:

            current_line += "{:>10}".format(i-1) + " state " + path[i-1]

            lines.append(current_line)

            current_line = "{:>10}".format(i)

            states[path[i-1]] += 1

    current_line += "{:>10}".format(len(path)) + " state " + path[i - 1]

    lines.append(current_line)

    states[path[i-1]] += 1

    file_name = "problem_2_output_" + str(output_file) + ".txt"

    text_file = open(file_name, "w")

    first_line = "State A: {}, State B: {}\n".format(states["A"], states["B"])

    text_file.write(first_line)

    for line in lines:

        text_file.write(line + "\n")


def main():

    file = sys.argv[1]

    params_file = sys.argv[2]

    data = parse_file(file)

    a_prob, b_prop, all_a, all_b = read_params(params_file)

    path = viterbi(data, a_prob, b_prop, all_a, all_b)

    new_file = file.replace("/", "_").replace(".", "_").strip()

    output(path, new_file)


if __name__ == "__main__":

    main()
