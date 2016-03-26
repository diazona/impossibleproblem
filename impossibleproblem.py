from itertools import chain
from math import trunc

def check_for_all_digits(a, b, n):
    '''Checks whether a and b and their difference, taken together, include all
    digits from 1 to 9 exactly n times each.'''
    counts = [0] * 9
    for c in chain(str(a), str(b), str(a - b)):
        if c == '0':
            return None
        else:
            counts[ord(c) - 49] += 1
    if all(count == n for count in counts):
        return str(a) + str(b) + str(a - b)
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
    for y in range(minY, maxY+1):
        for x in range(minX, trunc(y/2)):
            digits = check_for_all_digits(y, x, num_of_digits / 3)
            if digits is not None:
                yield frozenset((x, y, y-x))

def main():
    num_of_digits = 3

    try:
        solution_generator = find_solutions(num_of_digits)
    except ValueError:
        print("Not a valid number of digits!")
        return

    solutions = set()
    for i, sol in enumerate(solution_generator):
        solutions.add(sol)
        #print("{} - {} = {}".format(*sorted(sol, reverse=True)))

    successes = i + 1

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

    print("There were {} duplicates, by the way :)".format(successes - len(solutions)))

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
