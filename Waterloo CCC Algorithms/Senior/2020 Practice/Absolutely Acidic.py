# Absolutely Acidic

N = int(input())
readings = []

for i in range(N):
    nextInput = int(input())
    readings.append(nextInput)

frequencyList = []
highModeList = [0]
lowModeList = [-1]

for i in range(1000):
    frequencyList.append(0)

for i in range(N):
    frequencyList[readings[i] - 1] += 1

for i in range(len(frequencyList)):

    if frequencyList[i] > frequencyList[highModeList[0] - 1]:
        highModeList = [i + 1]

    elif frequencyList[i] == frequencyList[highModeList[0] - 1]:
        highModeList.append(i + 1)

    elif frequencyList[i] > frequencyList[lowModeList[0] - 1]:
        lowModeList = [i + 1]

    elif frequencyList[i] == frequencyList[lowModeList[0] - 1]:
        lowModeList.append(i + 1)

if max(frequencyList) == 1:
    diff = abs(max(readings) - min(readings))

else:
    diff = max(abs(max(highModeList) - min(lowModeList)), abs(max(lowModeList) - min(highModeList)))

print(str(diff))