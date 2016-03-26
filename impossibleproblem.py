from itertools import islice, permutations
from math import trunc

def find_solutions(num_of_digits):
    digits = '123456789' * int(num_of_digits / 3)
    for p in permutations(digits):
        i = iter(p)
        a = int(''.join(islice(i, num_of_digits)))
        b = int(''.join(islice(i, num_of_digits)))
        c = int(''.join(islice(i, num_of_digits)))
        if a > b > c and a - b == c:
            yield frozenset((a, b, c))

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

    print("There were {} duplicates, by the way :)".format(len(solutions) - len(set(solutions))))

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
