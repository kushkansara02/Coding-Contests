#Tournament Selection

game1 = input("")
game2 = input("")
game3 = input("")
game4 = input("")
game5 = input("")
game6 = input("")

wins = 0

if game1 == "W":
    wins += 1

if game2 == "W":
    wins += 1

if game3 == "W":
    wins += 1

if game4 == "W":
    wins += 1

if game5 == "W":
    wins += 1

if game6 == "W":
    wins += 1

if wins == 1 or wins == 2:
    print(3)

elif wins == 3 or wins == 4:
    print(2)

elif wins == 5 or wins == 6:
    print(1)

elif wins == 0:
    print(-1)