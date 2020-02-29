#Exactly Electrical

point1 = input("").split(" ")
point2 = input("").split(" ")
charge = int(input(""))

xdist = abs(int(point1[0]) - int(point2[0]))
ydist = abs(int(point1[1]) - int(point2[1]))
diff = abs(xdist - ydist)

if (xdist + ydist) > charge:
    ability = "N"

elif diff == 0:
    
    if charge%2 !=0:
        ability = "N"

    else:
        ability = "Y"

elif diff != 0:

    if diff%2 == 0:

        if charge%2 == 0:
            ability = "Y"

        else:
            ability = "N"

    elif diff%2 != 0:

        if charge%2 == 0:
            ability = "N"

        else:
            ability = "Y"

print(ability)
