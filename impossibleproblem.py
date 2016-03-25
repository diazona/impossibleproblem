from math import trunc

def check_for_all_digits(a, b, n):
    '''Checks whether a and b and their difference, taken together, include all
    digits from 1 to 9 exactly n times each.'''
    seq = str(a), str(b), str(a - b)
    digits = "".join(seq)
    goodChecks = 0
    for i in range(1,10):
        if digits.count(str(i)) == n:
            goodChecks += 1
    if goodChecks == 9:
        return digits
    else:
        return None

def find_solutions(num_of_digits):
    if num_of_digits == 3:
        minY = 381
        maxY = 987
        minX = 123
    elif num_of_digits == 6:
        minY = 246912
        maxY = 998877
        minX = 123123
    else:
        raise ValueError('invalid number of digits: {} should be 3 or 6'.format(num_of_digits))
    solutions = []
    for y in range(minY, maxY+1):
        for x in range(minX, trunc(y/2)):
            digits = check_for_all_digits(y, x, num_of_digits / 3)
            if digits is not None:
                solutions.extend([x, y-x])
    return solutions

def main():
    num_of_digits = int(input("please enter a number of digits, which is a multiple of 3"))

    try:
        solutions = find_solutions(num_of_digits)
    except ValueError:
        print("Not a valid number of digits!")
        return

    successes = len(solutions)

    print()
    print("I found: {} successful solution to your brainteaser".format(successes))
    if successes < 20:
        print("there were almost no solutions")
    elif successes < 100:
        print("there were not many solutions")
    elif successes < 1000:
        print("there were more than a hundred solutions it is definitely not impossible :)")
    else:
        print("that's a lot of successes")

    print("There were {} duplicates, by the way :)".format(len(solutions) - len(set(solutions))))

if __name__ == '__main__':
    main()
