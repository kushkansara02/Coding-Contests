# Pretty Average Primes

numTestCases = int(input())
testCases = []

for x in range(numTestCases):
    testInput = int(input())
    testCases.append(testInput)

def CheckPrime(num):

    prime = True

    for x in range(1, num):

        if num % x == 0 and (x != 1 and x != num):
            prime = False

    return prime

def Compute_AandB(num):
    a = num
    b = num
    averageVals = []

    while True:
        a -= 1
        b += 1
        if CheckPrime(a) and CheckPrime(b):
            break

    averageVals.append(a)
    averageVals.append(b)

    return averageVals

for x in range(numTestCases):
    print(str(Compute_AandB(testCases[x])[0]) + " " + str(Compute_AandB(testCases[x])[1]))