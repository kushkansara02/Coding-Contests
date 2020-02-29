#Are We There Yet?

distances = input("")
listDistances = distances.split(" ")

d1 = int(listDistances[0])
d2 = int(listDistances[1])
d3 = int(listDistances[2])
d4 = int(listDistances[3])

print(0, d1, d1 + d2, d1 + d2 + d3, d1 + d2 + d3 + d4)
print(d1, 0, d2, d2 + d3, d2 + d3 + d4)
print(d1 + d2, d2, 0, d3, d3 + d4)
print(d1 + d2 + d3, d2 + d3, d3, 0, d4)
print(d1 + d2 + d3 + d4, d2 + d3 + d4, d3 + d4, d4, 0)
