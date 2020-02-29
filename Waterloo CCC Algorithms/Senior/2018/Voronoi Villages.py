# Voronoi Villages

N = int(input())

villages = []

for x in range(N):
    nextVillage = int(input())
    villages.append(nextVillage)

def AverageOfTwoNums(x, y):
    return (x+y)/2

villages.sort()
neighborhoodBoundaries = []

for x in range(len(villages) - 1):
    neighborhoodBoundaries.append(AverageOfTwoNums(villages[x], villages[x+1]))

neighborhoodSize = []

for x in range(1, len(villages) - 1):
    leftSize = villages[x] - neighborhoodBoundaries[x - 1]
    rightSize = neighborhoodBoundaries[x] - villages[x]
    neighborhoodSize.append(leftSize + rightSize)

print(min(neighborhoodSize))