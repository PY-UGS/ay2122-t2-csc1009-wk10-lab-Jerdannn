def moduleCode(x):
    # Using Python 3.9, therefore,
    switch = {
        'CSC1006': 'Mathematics II',
        'CSC1007': 'Operating Systems',
        'CSC1008': 'Data Structures & Algorithms',
        'CSC1009': 'Object-Oriented Programming',
        'CSC1010': 'Computer Networks'
    }

    # Second argument is the default value
    return switch.get(x, "Invalid")


def oddNumber():
    # -1 starting from 102 to 66
    for i in range(102, 66, -1):
        # If i is an odd number
        if i % 2 != 0:
            print(i)


def main():
    module_code = input("Please enter the module code: ")
    module_name = moduleCode(module_code)
    print(module_name)
    oddNumber()


if __name__ == "__main__":
    main()
