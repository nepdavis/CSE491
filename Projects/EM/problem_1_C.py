import sys
import numpy as np


def parse_file(filename):

    all_series = []

    with open(filename) as f:

        for line in f:

            line = [int(i) for i in line.strip()]

            all_series.append(line)

    return all_series


def em(data):

    prob_a = .5
    prob_b = .5

    # params_a = np.random.dirichlet(np.ones(6), size=1)[0]
    # params_b = np.random.dirichlet(np.ones(6), size=1)[0]

    params_a = list(np.random.uniform(size = 6))
    params_b = list(np.random.uniform(size = 6))

    max_iter = 30

    for i in range(max_iter):

        # all_a = []
        # all_b = []

        for series in data:

            counts = np.array([series.count(i) for i in range(1, 7)])

            # print(counts)
            #
            # log_lik_a = sum([np.log(params_a[i - 1]) for i in series])
            # log_lik_b = sum([np.log(params_b[i - 1]) for i in series])
            #
            # print(log_lik_a)
            # print(log_lik_b)
            #
            # combined = np.exp(log_lik_a) + np.exp(log_lik_b)
            #
            # prob_a = np.exp(log_lik_a) / combined
            # prob_b = np.exp(log_lik_b) / combined
            #
            # print(combined)
            # print(prob_a)
            # print(prob_b)
            #
            # temp_params_a = [sum([np.log(params_a[i])] * counts[i]) for i in range(6)]
            # temp_params_b = [sum([np.log(params_b[i])] * counts[i]) for i in range(6)]
            #
            # params_a = np.array(np.exp(temp_params_a)) / prob_a
            # params_b = np.array(np.exp(temp_params_b)) / prob_b

            lik_a = sum([params_a[i - 1] for i in series])
            lik_b = sum([params_b[i - 1] for i in series])

            combined = lik_a + lik_b

            print(lik_a, lik_b, combined)

            prob_a = lik_a / combined
            prob_b = lik_b / combined

            temp_params_a = [sum([params_a[i]] * counts[i]) for i in
                             range(6)]

            temp_params_b = [sum([params_b[i]] * counts[i]) for i in range(6)]

            params_a = np.array(temp_params_a) / lik_a
            params_b = np.array(temp_params_b) / lik_b

        break

        # params_a = np.sum(all_a, 0) / np.sum(all_a)
        # params_b = np.sum(all_b, 0) / np.sum(all_b)

    return prob_a, prob_b, params_a, params_b


def output(first_params, second_params, dice_params):

    """
    Function to format probabilities and print them out
    :param first_params: probs for rolls of first die
    :param second_params: probs for rolls of second die
    :param dice_params: probs for each die
    :return: None (prints to screen)
    """

    text_file = open("problem_1_C_output.txt", "w")

    # formats each container as list of strings. [1:] gets rid of leading zero
    first_p = ["{:.4f}".format(i)[1:] for i in first_params]
    sec_p = ["{:.4f}".format(i)[1:] for i in second_params]
    dice_q = ["{:.2f}".format(i)[1:] for i in dice_params]

    # first line is probability names
    first_line = " " * 5 + "q" + " " * 5 +\
                 "   ".join(["p_"+str(i) for i in range(1, 7)])

    # second line is just dividers
    second_line = " " * 5 + "--" + " " * 4 +\
                  " ".join(["-" * 5 for _ in range(6)])

    # third line is probs for first die
    third_line = "A:  " + dice_q[0] + "   " + " ".join(first_p)

    # fourth line is probs for second die
    fourth_line = "B:  " + dice_q[1] + "   " + " ".join(sec_p)

    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)

    out = first_line + "\n" + second_line + "\n" + third_line + "\n" + \
          fourth_line

    text_file.write(out)

    text_file.close()


def main():

    file = sys.argv[1]

    data = parse_file(file)

    prob_a, prob_b, params_a, params_b = em(data)

    output(params_a, params_b, [prob_a, prob_b])


if __name__ == "__main__":

    main()

def temp(filename):

    data = parse_file(filename)

    prob_a, prob_b, params_a, params_b = em(data)

    output(params_a, params_b, [prob_a, prob_b])
