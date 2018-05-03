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

    params_a = list(np.random.uniform(size = 6))
    params_b = list(np.random.uniform(size = 6))

    max_iter = 30
    threshold = 0.01
    ll_old = 0

    for i in range(max_iter):

        all_a = []
        all_b = []

        probs_a = []
        probs_b = []

        ll_new = 0

        for line in data:

            counts = np.array([line.count(i) for i in range(1, 7)])

            ll_A = np.sum([counts * np.log(params_a)])
            ll_B = np.sum([counts * np.log(params_b)])

            denom = np.exp(ll_A) + np.exp(ll_B)
            w_A = np.exp(ll_A) / denom
            w_B = np.exp(ll_B) / denom

            probs_a.append(w_A)
            probs_b.append(w_B)

            all_a.append(np.dot(w_A, counts))
            all_b.append(np.dot(w_B, counts))

            # update complete log likelihood
            ll_new += w_A * ll_A + w_B * ll_B

        # M-step: update values for parameters given current distribution
        # [EQN 2]
        params_a = np.sum(all_a, 0) / np.sum(all_a)
        params_b = np.sum(all_b, 0) / np.sum(all_b)
        # print distribution of z for each x and current parameter estimate

        prob_a = sum(probs_a) / (sum(probs_a) + sum(probs_b))
        prob_b = sum(probs_b) / (sum(probs_a) + sum(probs_b))

        if np.abs(ll_new - ll_old) < threshold:

            break

        ll_old = ll_new

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
