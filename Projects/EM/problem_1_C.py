import sys


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

    params_a = [1/6] * 6
    params_b = [1/6] * 6

    max_iter = 30

    for i in range(max_iter):

        break

    return prob_a, prob_b, params_a, params_b


def output(first_params, second_params, dice_params):

    """
    Function to format probabilities and print them out
    :param first_params: probs for rolls of first die
    :param second_params: probs for rolls of second die
    :param dice_params: probs for each die
    :return: None (prints to screen)
    """

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


def main():

    file = sys.argv[1]

    data = parse_file(file)

    prob_a, prob_b, params_a, params_b = em(data)

    output(params_a, params_b, [prob_a, prob_b])


if __name__ == "__main__":

    main()
