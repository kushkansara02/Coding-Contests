#Raghu Alluri
#Date: 2019/03/26
#Problem 2: L-Systems Go
file = open('DATA10.txt', 'r')
data = file.readlines()
file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', '')

line1 = data[0].split()

initrules = []

rules = []

#R is the number of Rules
R = int(line1[0])
#T is the number of iterations
T = int(line1[1])
#A is the initial state of the string
A = line1[-1]

splitA = list(map(str, A)) #This splits the initial state string letters into a list occupying different indicies

initrules = [] #Original copy of rules
rules = [] #Copy of rules that is 2 dimensional

joinA = ''

#This for loop puts all the rules in a nested list with the character and the value seperated (2 dimensional array)
for i in range(len(data) - 1):
    
    rules.append(data[i + 1])
    initrules.append(data[i + 1])

    rules[i] = rules[i].split()

for i in range(T):

    for j in range(R):

        for k in range(len(splitA)):

            if splitA[k] == rules[j][0]:
                splitA[k] = rules[j][1]

    joinA = joinA.join(splitA)
    splitA = list(map(str, joinA))

#print(len(joinA))




                


