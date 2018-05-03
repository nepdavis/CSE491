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
    prob_b_b = [np.log2(i) for i in params[:6]]

    emissions_a = {k: np.log2(v) for k, v in params[6].items()}
    emissions_b = {k: np.log2(v) for k, v in params[7].items()}

    # Initialize viterbi tables
    viterbi_a = [prob_a + emissions_a[data[0]]]
    viterbi_b = [prob_b + emissions_b[data[0]]]

    # Run viterbi algorithm
    for i in range(1, len(data)):

        a = max(emissions_a[data[i]] + viterbi_a[i-1] + prob_a_a,
                emissions_a[data[i]] + viterbi_b[i-1] + prob_b_a)

        b = max(emissions_b[data[i]] + viterbi_a[i-1] + prob_a_b,
                emissions_b[data[i]] + viterbi_b[i-1] + prob_b_b)

        viterbi_a.append(a)
        viterbi_b.append(b)

    print(viterbi_a[718:723])
    print(viterbi_b[718:723])

    return viterbi_a, viterbi_b


def traceback(viterbi_a, viterbi_b):

    states = {"A": "B", "B": "A"}

    lines = []

    current_line = "{:>10}".format(1)

    state_numbers = {"A": 0, "B": 0}

    if viterbi_a[0] > viterbi_b[0]:

        current_state = "A"

    else:

        current_state = "B"

    for i in range(1, len(viterbi_a)):

        if viterbi_a[i] > viterbi_b[i]:

            if current_state != "A":

                current_line += "{:>10}".format(i) + " state " + current_state

                lines.append(current_line)

                current_line = "{:>10}".format(i + 1)

                state_numbers[current_state] += 1

                current_state = states[current_state]

        #elif viterbi_b[i] > viterbi_a[i] and current_state != "B":
        else:

            if current_state != "B":

                current_line += "{:>10}".format(i) + " state " + current_state

                lines.append(current_line)

                current_line = "{:>10}".format(i + 1)

                state_numbers[current_state] += 1

                current_state = states[current_state]

    current_line += "{:>10}".format(i + 1) + " state " + current_state
    lines.append(current_line)

    return lines, state_numbers


def output(lines, states):

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

    hmm_a, hmm_b = viterbi(data, params)

    output_lines, states = traceback(hmm_a, hmm_b)

    output(output_lines, states)


if __name__ == "__main__":

    main()
