#Sunflowers

#all orientations are degrees rotated CLOCKWISE

N = int(input(""))
nCounter = 1
tableArray = [
    ]

while nCounter <= N:
    nextRow = input("")
    tableArray.append(nextRow.split(" "))
    nCounter += 1

if tableArray[0][0] < tableArray[0][N-1]:
    
    if tableArray[0][0] < tableArray[N-1][0]:
        orientation = 360

    elif tableArray[0][0] > tableArray[N-1][0]:
        orientation = 270

if tableArray[0][0] > tableArray[0][N-1]:

    if tableArray[0][0] < tableArray[N-1][0]:
        orientation = 90

    elif tableArray[0][0] > tableArray[N-1][0]:
        orientation = 180

