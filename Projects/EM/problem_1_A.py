import sys


def parse_file(filename):

    """
    Function to read in the file and parse it line by line. Stores counts of
    die choices and their respective rolls. Returns counts for each die, and
    the number of rolls of each number for each die.
    :param filename: file of rolls to open
    :return: the three count containers
    """

    rolls_dice_a = []
    rolls_dice_b = []

    dice_dict_count = {"A": 0, "B": 0}

    with open(filename) as f:

        for line in f:

            temp_die, temp_rolls = line.strip().split(" ")

            if temp_die == "A":

                dice_dict_count[temp_die] += 1

                rolls_dice_a.extend([int(i) for i in temp_rolls])

            else:

                dice_dict_count[temp_die] += 1

                rolls_dice_b.extend([int(i) for i in temp_rolls])

    return rolls_dice_a, rolls_dice_b, dice_dict_count


def mle(first_rolls, second_rolls, dice_rolls):

    """

    :param first_rolls: list of rolls for first dice
    :param second_rolls: list of rolls for second dice
    :param dice_rolls: dict of each die and its count
    :return: list of probs for first die rolls, list of probs for second die
             rolls, and list of probs for each die
    """

    first_probs = []
    second_probs = []

    dice_probs = []

    for roll in range(1, 7):

        first_probs.append(first_rolls.count(roll) / len(first_rolls))

        second_probs.append(second_rolls.count(roll) / len(second_rolls))

    for count in dice_rolls.values():

        dice_probs.append(count / sum(dice_rolls.values()))

    return first_probs, second_probs, dice_probs


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

    """
    Runs program functions
    :return: None
    """

    file = sys.argv[1]

    rolls_a, rolls_b, die_counts = parse_file(filename = file)

    first_params, second_params, dice_params = em(rolls_a, rolls_b, die_counts)

    output(first_params, second_params, dice_params)


if __name__ == "__main__":

    main()
