from math import trunc

def solver(number,number2, numberofdigits):
    seq = str(number),str(number2), str(number - number2)
    digits = "".join(seq)
    goodChecks = 0
    count= numberofdigits/3
    for i in range(1,10):
        if digits.count(str(i)) == count:
            goodChecks += 1
    if goodChecks == 9:
        return digits
    else:
        return False

middlenumber =[]
successes = 0
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


for y in range(minY, maxY+1):
    numberlist = []
    if y%100 == 0:
        print(y)
    for x in range(minX,trunc(y/2)):
        digits = solver(y,x,num_of_digits)
        if digits is not False:
            successes += 2
            print(digits)
            numberlist.extend([x,y-x])
            middlenumber.extend([x, y-x])

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

print("There were ", len(middlenumber) - len(set(middlenumber)) , " duplicates, by the way :)")