#Cold Compress

N = int(input())
inputList = []
counterList = []

for x in range(N):
    inputLine = input()
    inputList.append(inputLine)

for y in range(N):
    counterListTemp = []
    counter = 1

    for n in range(1,len(inputList[y])):

        if inputList[y][n] == inputList[y][n - 1]:
            counter += 1

            if n == len(inputList[y]) - 1:
                counterListTemp.append(counter)

        else:
            counterListTemp.append(counter)
            counter = 1

    counterList.append(counterListTemp)

n = len(counterList)

for x in range(n):
    printLine = ""
    indexCount = 0

    for y in range(1,len(counterList[x])):
        indexCount += counterList[x][y]
        printLine += str(counterList[x][y]) + " "
        printLine += str(inputList[x][indexCount - 1]) + " "

    print(printLine)
