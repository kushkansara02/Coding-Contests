# Searching for Strings

needleString = "abc"
haystackString = "abccbabd"
needleList = []

for char in needleString:
    needleList.append(char)

def Join(mainList):
    joined = ""

    for item in mainList:
        joined += item

    return joined

def CalculateAllPermutations(givenString, currentPermutations):
    global permutations

    n = len(givenString)

    for x in range(1, n):
        newString = []

        for char in givenString:
            newString += char

        copy = givenString[x - 1]
        newString[x - 1] = givenString[x]
        newString[x] = copy

        if Join(newString) not in currentPermutations:
            currentPermutations.append(Join(newString))

            newPermutations = CalculateAllPermutations(newString, currentPermutations)

            if newPermutations != currentPermutations:
                for perm in newPermutations:
                    if Join(perm) not in currentPermutations and Join(perm) != None:
                        currentPermutations.append(perm)

    return currentPermutations


permutations = CalculateAllPermutations(needleList, [needleString])

counter = 0

for perm in permutations:
    if Join(perm) != None:
        if Join(perm) in haystackString:
            counter += 1

print(counter)
