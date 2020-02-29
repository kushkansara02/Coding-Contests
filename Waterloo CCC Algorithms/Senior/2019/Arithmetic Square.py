# Arithmetic Square

# r1 = input().split(" ")
# r2 = input().split(" ")
# r3 = input().split(" ")
#
# referenceAllNumbers = r1 + r2 + r3
# allNumbers = referenceAllNumbers
#
# col1 = [r1[0], r2[0], r3[0]]
# col2 = [r1[1], r2[1], r3[1]]
# col3 = [r1[2], r2[2], r3[2]]
#
# unitConversions = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

allNumbers = ["8", "9", "10", "16", "18", "20", "24", "X", "30"]


def assignColumnVals(list):
    column1 = [list[0], list[3], list[6]]
    column2 = [list[1], list[4], list[7]]
    column3 = [list[2] + list[5], list[8]]
    return column1, column2, column3


def assignRowVals(list):
    row1 = [list[0], list[1], list[2]]
    row2 = [list[3], list[4], list[5]]
    row3 = [list[6], list[7], list[8]]
    return row1, row2, row3


def FindX():

    xLocations = []

    for x in range(len(allNumbers)):

        if allNumbers[x] == "X":
            xLocations.append(x)

    return xLocations


def CheckIfSequence(list):
    if (int(list[2]) - int(list[1])) == (int(list[1]) - int(list[0])):
        return True
    else:
        return False


def rec(listOfNum):
    row1, row2, row3 = assignRowVals(listOfNum)
    column1, column2, column3 = assignColumnVals(listOfNum)

    if CheckIfSequence(row1) and CheckIfSequence(row2) and CheckIfSequence(row3) and CheckIfSequence(column1) and CheckIfSequence(column2) and CheckIfSequence(column3):
        return listOfNum

    for x in xAllLocations:
        listOfNum[x] += 1
        output = rec(listOfNum)

        if output:
            return output


xAllLocations = FindX()

for x in xAllLocations:
    allNumbers[x] = 27

finalAns = rec(allNumbers)

print(finalAns)