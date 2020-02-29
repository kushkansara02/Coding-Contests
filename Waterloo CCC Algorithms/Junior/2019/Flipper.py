#Flipper

originalGrid = [1, 2, 3, 4]

def switch(orientationFlip, numberList):

    if orientationFlip == "horizontal":
        newNumberList = [numberList[2], numberList[3], numberList[0], numberList[1]]
        numberList = newNumberList

    elif orientationFlip == "vertical":
        newNumberList = [numberList[1], numberList[0], numberList[3], numberList[2]]
        numberList = newNumberList

    return numberList

flipSeries = input()

for char in flipSeries:

    if char == "H":
        originalGrid = switch("horizontal", originalGrid)

    elif char == "V":
        originalGrid = switch("vertical", originalGrid)

print(str(originalGrid[0]) + " " + str(originalGrid[1]))
print(str(originalGrid[2]) + " " + str(originalGrid[3]))