#Magic Squares

Magic = False

input1 = input("")
input2 = input("")
input3 = input("")
input4 = input("")

row1 = input1.split(" ")
row2 = input2.split(" ")
row3 = input3.split(" ")
row4 = input4.split(" ")

row1sum = int(row1[0]) + int(row1[1]) + int(row1[2]) + int(row1[3])
row2sum = int(row2[0]) + int(row2[1]) + int(row2[2]) + int(row2[3])
row3sum = int(row3[0]) + int(row3[1]) + int(row3[2]) + int(row3[3])
row4sum = int(row4[0]) + int(row4[1]) + int(row4[2]) + int(row4[3])

col1sum = int(row1[0]) + int(row2[0]) + int(row3[0]) + int(row4[0])
col2sum = int(row1[1]) + int(row2[1]) + int(row3[1]) + int(row4[1])
col3sum = int(row1[2]) + int(row2[2]) + int(row3[2]) + int(row4[2])
col4sum = int(row1[3]) + int(row2[3]) + int(row3[3]) + int(row4[3])

if row1sum == row2sum == row3sum == row4sum == col1sum == col2sum == col3sum == col4sum:
    Magic = True

if Magic:
    print("magic")

if not Magic:
    print("not magic")