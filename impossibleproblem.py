from itertools import product

def digits_solver():
    column = [(x, a, d, (x + a + d) % 10, (x + a + d) // 10)
              for x, a, d in product(range(2), range(1, 10), range(1, 10))
              if len(set([a, d, (x + a + d) % 10])) == 3 and (x + a + d) % 10 != 0]
    first_column = [(x, a, d, g) for x, a, d, g, z in column if z == 0 and a < d]
    for x, a, d, g in first_column:
        second_column = [(y, b, e, h) for y, b, e, h, xx in column if xx == x and not set([a,d,g]) & set([b,e,h])]
        for y, b, e, h in second_column:
            third_column = [(r, c, f, i) for r, c, f, i, yy in column
                            if yy == y and not set([a,d,g,b,e,h]) & set([c,f,i]) and r == 0 ]
            for _, c, f, i  in third_column:
                yield (100 * g + 10 * h + i, 100 * d + 10 * e + f, 100 * a + 10 * b + c)


def main():
    num_of_digits = 3

    try:

        solution_generator = digits_solver()
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

    print("There were {} duplicates, by the way :)".format(successes - len(set(solutions))))

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
