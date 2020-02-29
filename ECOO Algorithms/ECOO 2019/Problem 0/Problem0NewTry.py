#Raghu Alluri
#Date: 2019/3/27
#Problem 0: Rolling the Dice

file = open('DATA00.txt', 'r')
data = file.readlines()
file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', '')

line1 = data[0].split() #['3', '3']
line2 = data[1].split() #['1', '3', '1']

D = int(line1[0]) #3
N = int(line1[1]) #3

#Length of rolls list will always have to be N

rollappearance = []

#This generates an array of predetermined length but empty i.e. [0, 0, 0]
for i in range(N):
    rollappearance.append(0)

#Looping through to add values to rolls.
#   [2, 0, 1]
#   1    2    3

for i in range(D + 1):

    for x in range(N):
        if i == int(line2[x]):
            rollappearance[i - 1] += 1

sideLeastRolls = rollappearance.index(min(rollappearance)) + 1
sideGreatestRolls = rollappearance.index(max(rollappearance)) + 1

print(str(sideLeastRolls) + ' ' + str(sideGreatestRolls))









