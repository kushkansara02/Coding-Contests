# High Tide

N = int(input())
totalList = input().split()

for x in range(len(totalList)):
    totalList[x] = int(totalList[x])

totalList.sort()

allLows = []
allHighs = []

orderedList = []

for i in range(N):
    limit = 0

    if len(totalList) % 2 == 0:
        limit = N/2 - 1

    else:
        limit = N/2

    if i <= limit:
        allLows.append(int(totalList[i]))

    else:
        allHighs.append(int(totalList[i]))

allLows.sort(reverse = True)

for i in range(len(allLows)):
    orderedList.append(allLows[i])

    try:
        orderedList.append(allHighs[i])

    except:
        continue

output = ""

for val in orderedList:
    output += str(val) + " "

output = output[:-1]

print(output)
