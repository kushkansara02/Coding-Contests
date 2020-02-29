#Shifty Sum

N = int(input(""))
k = int(input(""))
total = N

for i in range(k):
    sN = str(N) + "0"
    N = int(sN)
    total += N

print(total)
