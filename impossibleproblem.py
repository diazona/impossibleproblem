from math import trunc

def check_for_all_digits(a, b, n):
    '''Checks whether a and b and their difference, taken together, include all
    digits from 1 to 9 exactly n times each.'''
    seq = str(a),str(b), str(a - b)
    digits = "".join(seq)
    goodChecks = 0
    for i in range(1,10):
        if digits.count(str(i)) == n:
            goodChecks += 1
    if goodChecks == 9:
        return digits
    else:
        return False

def find_solutions(minX, minY, maxY, num_of_digits):
    solutions = []
    successes = 0
    for y in range(minY, maxY+1):
        numberlist = []
        if y%100 == 0:
            print(y)
        for x in range(minX,trunc(y/2)):
            digits = check_for_all_digits(y, x, num_of_digits / 3)
            if digits is not False:
                successes += 2
                print(digits)
                numberlist.extend([x,y-x])
                solutions.extend([x, y-x])
    return solutions, successes

def main():
    num_of_digits = int(input("please enter a number of digits, which is a multiple of 3"))
    if num_of_digits == 3:
        minY = 381
        maxY = 987
    if num_of_digits == 6:
        minY =246912
        maxY = 998877

    if num_of_digits == 3:
        minX = 123
    if num_of_digits == 6:
        minX =123123

    solutions, successes = find_solutions(minX, minY, maxY, num_of_digits)

    print("")
    print("I found: ", successes, " successful solution to your brainteaser")
    if successes < 20:
        print("there were almost no solutions")
    elif successes < 100:
        print("there were not many solutions")
    elif successes < 1000:
        print("there were more than a hundred solutions it is definitely not impossible :)")
    else:
        print("that's a lot of successes")

    print("There were ", len(solutions) - len(set(solutions)) , " duplicates, by the way :)")

if __name__ == '__main__':
    main()
