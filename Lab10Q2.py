def average(x, y):
    return float((x + y)/2)


def main():
    print("Please add a space between each number")
    first_num, second_num \
        = input("Please enter two numbers: ").split()
    num_average = average(int(first_num), int(second_num))
    print("The average of "
          "{} and {} is {}".format(first_num,
                                   second_num, num_average))


if __name__ == '__main__':
    main()
