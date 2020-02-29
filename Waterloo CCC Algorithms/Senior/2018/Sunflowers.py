# Sunflowers

N = int(input())

rotatedTable = []

for x in range(N):
    nextRow = input().split()
    rotatedTable.append(nextRow)

def rotate2DArray(array):
    global rotatedTable

    newRotatedArray = []
    for i in range(N):
        horizontal = []
        for j in range(N):
            horizontal.append(False)
        newRotatedArray.append(horizontal)

    for x in range(N):
        for y in range(N):
            newRotatedArray[x][y] = rotatedTable[N - y - 1][x]

    rotatedTable = newRotatedArray

if int(rotatedTable[0][0]) > int(rotatedTable[0][1]) and int(rotatedTable[0][0]) < int(rotatedTable[1][0]):
    rotate2DArray(rotatedTable)
    rotate2DArray(rotatedTable)
    rotate2DArray(rotatedTable)

elif int(rotatedTable[0][0]) > int(rotatedTable[0][1]) and int(rotatedTable[0][0]) > int(rotatedTable[1][0]):
    rotate2DArray(rotatedTable)
    rotate2DArray(rotatedTable)

elif int(rotatedTable[0][0]) < int(rotatedTable[0][1]) and int(rotatedTable[0][0]) > int(rotatedTable[1][0]):
    rotate2DArray(rotatedTable)

for line in rotatedTable:
    output = ""
    for x in range(len(line)):
        output += line[x] + " "
    output = output[:-1]
    print(output)