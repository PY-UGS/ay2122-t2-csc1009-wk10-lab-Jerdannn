def moduleCode(x):
    # Using Python 3.9, therefore,
    switch = {
        1006: 'Mathematics II',
        1007: 'Operating Systems',
        1008: 'Data Structures & Algorithms',
        1009: 'Object-Oriented Programming',
        1010: 'Computer Networks'
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
    # [3:] prints out the code after CSC (which is what we need)
    module_name = moduleCode(int(module_code[3:]))
    print(module_name)
    oddNumber()


if __name__ == "__main__":
    main()
