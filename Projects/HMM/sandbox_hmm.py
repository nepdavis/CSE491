import sys
import numpy as np


def parse_file(filename):

    data = ""

    with open(filename) as f:

        for line in f:

            if line.strip()[0] == ">":

                continue

            data += line.strip()

    return data.upper()


def read_params(filename):

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

    prob_a_a, prob_a_b = [float(i) for i in lines[2].split()[:2]]

    prob_emission_a = {emissions[i]: float(lines[2].split()[2:][i]) for i in range(4)}

    # Parse fourth line

    prob_b_a, prob_b_b = [float(i) for i in lines[3].split()[:2]]

    prob_emission_b = {emissions[i]: float(lines[3].split()[2:][i]) for i in range(4)}

    return prob_a, prob_b, prob_a_a, prob_a_b, prob_b_a, \
        prob_b_b, prob_emission_a, prob_emission_b


def viterbi(data, params):

    # Transform probabilities to log space
    prob_a, prob_b, prob_a_a, prob_a_b, prob_b_a, \
    prob_b_b = [np.log(i) for i in params[:6]]

    emissions_a = {k: np.log(v) for k, v in params[6].items()}
    emissions_b = {k: np.log(v) for k, v in params[7].items()}

    emissions = [emissions_a, emissions_b]
    total_probs = [prob_a, prob_b]

    transitions = np.array([[prob_a_a, prob_a_b],
                            [prob_b_a, prob_b_b]])

    nrow, ncol = 2, len(data)

    mat = np.zeros(shape = (nrow, ncol), dtype = float)  # prob
    matTb = np.zeros(shape = (nrow, ncol), dtype = int)  # backtrace

    # Fill in first column
    for i in range(0, nrow):

        mat[i, 0] = emissions[i][data[0]] + total_probs[i]

    # Fill in rest of prob and Tb tables
    for j in range(1, ncol):

        for i in range(0, nrow):

            ep = emissions[i][data[j]]

            mx, mxi = mat[0, j - 1] + transitions[0, i] + ep, 0

            for i2 in range(1, nrow):

                pr = mat[i2, j - 1] + transitions[i2, i] + ep

                if pr > mx:

                    mx, mxi = pr, i2

            mat[i, j], matTb[i, j] = mx, mxi

    omx, omxi = mat[0, ncol - 1], 0

    for i in range(1, nrow):

        if mat[i, ncol - 1] > omx:

            omx, omxi = mat[i, ncol - 1], i

    # Backtrace
    i, p = omxi, [omxi]

    for j in range(ncol - 1, 0, -1):

        i = matTb[i, j]
        p.append(i)

    path = ["A" if i == 0 else "B" for i in p]

    return path[::-1]


def output(path):
    lines = []
    states = {"A": 0, "B": 0}
    current_line = "{:>10}".format(1)

    for i in range(1, len(path)):

        if path[i - 1] != path[i]:
            current_line += "{:>10}".format(i - 1) + " state " + path[i - 1]

            lines.append(current_line)

            current_line = "{:>10}".format(i)

            states[path[i - 1]] += 1

    current_line += "{:>10}".format(len(path)) + " state " + path[i - 1]

    lines.append(current_line)

    states[path[i - 1]] += 1

    text_file = open("problem_2_output.txt", "w")

    first_line = "State A: {}, State B: {}\n".format(states["A"], states["B"])

    text_file.write(first_line)

    for line in lines:
        text_file.write(line + "\n")


def main():

    file = sys.argv[1]

    params_file = sys.argv[2]

    data = parse_file(file)

    params = read_params(params_file)

    path = viterbi(data, params)

    output(path)


if __name__ == "__main__":

    main()
