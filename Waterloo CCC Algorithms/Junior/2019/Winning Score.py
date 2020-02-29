#Winning Score

a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

ApplesScore = 3*a3 + 2*a2 + 1*a1
BananasScore = 3*b3 + 2*b2 + 1*b1

if ApplesScore > BananasScore:
    print("A")

elif BananasScore > ApplesScore:
    print("B")

else:
    print("T")
