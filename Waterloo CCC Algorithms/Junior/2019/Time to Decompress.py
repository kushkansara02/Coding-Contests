#Time to Decompress

L = int(input(""))

for x in range(L):
    eval("l" + str(x+1) + " = input("")")

for y in range(L):
    n = 0
    finalLinePrint = ""

    eval("l" + str(y + 1) + ".split(" ")")
    eval("times = int(l" + str(y + 1) + "[0])")
    eval("char = l" + str(y + 1) + "[1]")

    while n < times:
        finalLinePrint += char

    print(finalLinePrint)