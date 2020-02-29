# Nailed It

def NumOfMode(mainList):

    frequencyList = []

    for i in range(len(mainList)):
        frequencyList.append(mainList.count(mainList[i]))

    maxes = [mainList[0]]
    max = 0

    for i in range(1, len(frequencyList)):

        if frequencyList[i] > frequencyList[max]:
            maxes = [mainList[i]]
            max = i

        elif frequencyList[i] == frequencyList[max]:
            maxes.append(mainList[i])

    refinedMaxes = []

    for num in maxes:
        if num not in refinedMaxes:
            refinedMaxes.append(num)

    lengthOfFence = frequencyList[max]
    lengthOfModeList = len(refinedMaxes)

    return [lengthOfFence, lengthOfModeList]


N = int(input())
boardLengths = input().split()

sums = []

for i in range(N):
    for j in range(i + 1, N):
        sums.append(int(boardLengths[i]) + int(boardLengths[j]))

length, ways = NumOfMode(sums)

print(str(length) + " " + str(ways))