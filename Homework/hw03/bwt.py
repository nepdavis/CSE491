import time


def bwt():

    pass


def main():

    start_time = time.time()

    end_time = time.time() - start_time

    runtime_str = "The runtime of this program was {:5f} " \
                  "seconds".format(end_time)

    runtime_file = open("runtime.txt", "w")

    runtime_file.write(runtime_str)

    runtime_file.close()


if __name__ == "__main__":

    main()
