#Problem 1: Free Shirts
with open("DATA11.txt") as file:
    data = file.readlines()
    file.close()
for x in range(len(data)):
    data[x] = data[x].replace("\n", "")

for i in range(0,int(len(data)),2):
    line1 = data[i].split()
    events = data[i+1].split()

    clean = int(line1[0])
    m = int(line1[1])
    d = int(line1[2])
    dirty = 0
    laundry = 0

    for j in range(d):
        if clean == 0:
            clean = dirty
            dirty = 0
            laundry += 1
        if str(j+1) in events:
            for k in range(m):
                if events[k]==str(j+1):
                    clean += 1
        clean -= 1
        dirty += 1

    print(laundry)
