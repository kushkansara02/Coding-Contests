# RoboThieves

dimensions = input().split()
yLength = int(dimensions[0])
xLength = int(dimensions[1])

layout = []

for i in range(yLength):
    nextInput = input()
    layout.append(nextInput)

robotLocation = []
wallLocations = []
emptyLocations = []

for y in range(yLength):

    for x in range(xLength):

        if layout[y][x] == "S":
            robotLocation.append(y)
            robotLocation.append(x)

        elif layout[y][x] == "W":
            wallLocations.append([y, x])

        elif layout[y][x] == ".":
            emptyLocations.append([y,x])


def scanSurroundings(yCord, xCord):
    possibleMoves = []

    if layout[yCord - 1][xCord] == ".":
        possibleMoves.append([yCord - 1, xCord])

    if layout[yCord][xCord - 1] == ".":
        possibleMoves.append([yCord, xCord - 1])

    if layout[yCord + 1][xCord] == ".":
        possibleMoves.append([yCord + 1, xCord])

    if layout[yCord][xCord + 1] == ".":
        possibleMoves.append([yCord, xCord + 1])

    return possibleMoves


def checkIfPossible(robotLocation, yCord, xCord, count, previousLocation):

    possibleMoves = scanSurroundings(robotLocation[0], robotLocation[1])
    countList = []

    if previousLocation in possibleMoves:
        possibleMoves.remove(previousLocation)

    for cord in possibleMoves:

        if cord[0] == yCord and cord[1] == xCord:
            countList.append(count + 1)

        else:
            next = checkIfPossible(cord, yCord, xCord, count + 1, robotLocation)
            if next != -1:
                countList.append(next)

    if len(countList) > 0:
        return min(countList)

    else:
        return -1


for space in emptyLocations:
    print(checkIfPossible(robotLocation, space[0], space[1], 0, [-1, -1]))

