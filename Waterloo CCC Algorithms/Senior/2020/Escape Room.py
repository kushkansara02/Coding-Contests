# Escape Room

yLength = int(input())
xLength = int(input())
layout = []

startingSpot = [0, 0]
targetSpot = [yLength - 1, xLength - 1]

for i in range(yLength):
    nextVal = input().split()
    layout.append(nextVal)

def Factorize(num):

    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            if i <= yLength and int(num / i) <= xLength:
                factors.append([i, int(num / i)])

    return factors

def move(currentSpot, targetSpot, previousSpots):

    currentSpotVal = int(layout[int(currentSpot[0])][int(currentSpot[1])])
    previousSpots.append([int(currentSpot[0]), int(currentSpot[1])])
    possibleJumps = Factorize(currentSpotVal)

    if len(possibleJumps) > 0:
        for cord in possibleJumps:

            if [cord[0] - 1, cord[1] - 1] == targetSpot:
                print("yes")
                quit()

            elif [cord[0] - 1, cord[1] - 1] in previousSpots:
                break

            else:
                move([cord[0] - 1, cord[1] - 1], targetSpot, previousSpots)

move(startingSpot, targetSpot, [startingSpot])

print("no")