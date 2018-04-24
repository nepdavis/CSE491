import sys


def parse_params(filename):

    all_dicts = []

    with open(filename) as f:

        for line in f:

            params = line.strip().split()

            temp_dict = {"die": float(params[0])}

            temp_dict.update({i: float(params[i]) for i in range(1, 7)})

            all_dicts.append(temp_dict)

    return all_dicts


def probability(series, params):

    prob = 1

    for result in series:

        prob *= params[result]

    return prob * params["die"]


def bayes(filename, params_a, params_b):

    roll_results = []

    with open(filename) as f:

        for line in f:

            rolls = [int(i) for i in line.strip()]

            marg_a = probability(rolls, params_a)
            marg_b = probability(rolls, params_b)

            prob_a = marg_a / (marg_a + marg_b)
            prob_b = marg_b / (marg_a + marg_b)

            if prob_a > prob_b:

                roll_results.append(("A", prob_a))

            else:

                roll_results.append(("B", prob_b))

    return roll_results


def output(results):

    for i, line in enumerate(results):

        print("Sample {}: {}, posterior probability of {:.4f}".format(i + 1,
                                                                      line[0],
                                                                      line[1]))


def main():

    file_param = sys.argv[1]
    file_counts = sys.argv[2]

    params_a, params_b = parse_params(file_param)

    results = em(file_counts, params_a, params_b)

    output(results)


if __name__ == "__main__":

    main()
