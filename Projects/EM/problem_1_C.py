import sys
import numpy as np


def parse_file(filename):

    """
    Function to parse data
    :param filename: data filename
    :return: data as a list of lines
    """

    all_series = []

    with open(filename) as f:

        for line in f:

            line = [int(i) for i in line.strip()]

            all_series.append(line)

    f.close()

    return all_series


def em(data):

    """
    EM algorithm to determine optimal parameters
    :param data: data to perform EM on
    :return: parameters
    """

    # starting equal probabilities
    prob_a = .5
    prob_b = .5

    # generate random parameters
    params_a = list(np.random.uniform(size = 6))
    params_b = list(np.random.uniform(size = 6))

    # set max iteration to 30, threshold to .01, and null loglik to 0
    max_iter = 30
    threshold = 0.01
    loglik_0 = 0

    # for i in max iterations
    for i in range(max_iter):

        # create empty lists to hold parameters
        all_a = []
        all_b = []

        probs_a = []
        probs_b = []

        # new log likelihood of iteration
        loglik_i = 0

        # for line in data
        for line in data:

            # get counts of rolls
            counts = np.array([line.count(i) for i in range(1, 7)])

            # generate sums
            loglik_a = np.sum([counts * np.log(params_a)])
            loglik_b = np.sum([counts * np.log(params_b)])

            # create denominator
            total = np.exp(loglik_a) + np.exp(loglik_b)

            # get new parameters
            new_prob_a = np.exp(loglik_a) / total
            new_prob_b = np.exp(loglik_b) / total

            # keep track of parameters
            probs_a.append(new_prob_a)
            probs_b.append(new_prob_b)

            # keep track of dot products between parameters and counts
            all_a.append(np.dot(new_prob_a, counts))
            all_b.append(np.dot(new_prob_b, counts))

            # update complete log likelihood
            loglik_i += new_prob_a * loglik_a + new_prob_b * loglik_b

        # using all of the sums, get new parameters by seeing proportions
        params_a = np.sum(all_a, 0) / np.sum(all_a)
        params_b = np.sum(all_b, 0) / np.sum(all_b)

        # new probs for each die is the expected value
        prob_a = sum(probs_a) / (sum(probs_a) + sum(probs_b))
        prob_b = sum(probs_b) / (sum(probs_a) + sum(probs_b))

        # if the difference is less than our threshold
        if np.abs(loglik_i - loglik_0) < threshold:

            # end the algorith, we've converged
            break

        # update old log likelihood
        loglik_0 = loglik_i

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