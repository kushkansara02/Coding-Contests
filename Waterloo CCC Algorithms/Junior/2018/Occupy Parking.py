#Occupy Parking

N = int(input(""))
yesterday = input("")
today = input("")
counter = 0

for i in range(N):

    if yesterday[i] == "C":

        if today[i] == "C":
            counter += 1

print(counter)
