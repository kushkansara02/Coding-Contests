#Quadrant Selection

x = int(input(""))
y = int(input(""))

if x > 0 and y > 0:
    quadrant = 1

elif x < 0 and y < 0:
    quadrant = 3

elif x < 0 and y > 0:
    quadrant = 2

elif x > 0 and y < 0:
    quadrant = 4

else:
    quadrant = None

print(quadrant)
