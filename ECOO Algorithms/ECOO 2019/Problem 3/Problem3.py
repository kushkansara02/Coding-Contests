with open("DATA11.txt") as file:
    data1 = file.readline()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

J = data[0].split()[0]
W = data[0].split()[1]
H = data[0].split()[2]


data.remove(0)

def Clear(xcor):
    for i in range(J):
        if data[H - 2 - i][xcor - 1] == "@":
          return False

    if data[H - 2 - J][xcor] == "@":
        return False
    else:
        return True

def Output(data):
    counter = 0

    for char in data[H - 2]:
        if char == "L":
            Lcoor = counter
        elif char == "G":
            Gcoor = counter
        counter += 1

    for xcor in range(Lcoor + 1, Gcoor + 1):
        if data[H - 2][xcor] == "@":
            if not Clear(xcor):
                return xcor + 1
        elif xcor == Gcoor:
            return "CLEAR"
print(Output(data))
