# Surmising a Sprinter's Speed

N = int(input())
allVals = []

for i in range(N):
    nextVal = input().split()
    allVals.append([int(nextVal[0]), int(nextVal[1])])

allVals.sort()

speeds = []

for i in range(N - 1):
    nextSpeed = abs(int(allVals[i + 1][1]) - int(allVals[i][1])) / (int(allVals[i + 1][0]) - int(allVals[i][0]))
    speeds.append(nextSpeed)

print(max(speeds))
