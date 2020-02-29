# Flipper

transformationSequence = input()

numberGrid = [1, 2, 3, 4]

def varSwap(index1, index2):
    copy = numberGrid[index1]
    numberGrid[index1] = numberGrid[index2]
    numberGrid[index2] = copy

def Flip(orientation):

    if orientation == "V":
        varSwap(0, 1)
        varSwap(2, 3)
    else:
        varSwap(0, 2)
        varSwap(1, 3)

for x in range(len(transformationSequence)):
    Flip(transformationSequence[x])

print(str(numberGrid[0]) + " " + str(numberGrid[1]))
print(str(numberGrid[2]) + " " + str(numberGrid[3]))