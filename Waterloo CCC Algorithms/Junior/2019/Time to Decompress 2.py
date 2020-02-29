#Time to Decompress

L = int(input())

inputList = []

for x in range(L):
    lineInput = input()
    theList = lineInput.split(" ")
    inputList.append(theList)

for y in range(L):
    finalPrint = ""

    times = int(inputList[y][0])
    char = inputList[y][1]

    for x in range(times):
        finalPrint = finalPrint + char

    print(finalPrint)