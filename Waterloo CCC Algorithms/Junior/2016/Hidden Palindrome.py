#Hidden Palindrome

Input = input("")
done = False
n = 1
lengthy = 0

change = False
double = False
single = False

for i in range(len(Input)):

    if Input[i] == Input[i - 1]:
        n = 0
        change = True
        double = True

        while not done:
            if Input[i + n] == Input[i - (n + 1)] and i > 2:
                n += 1

            else:
                done = True

    elif Input[i] == Input[i + 1]:
        n = 0
        done = False
        change = True
        double = True

        while not done:
            if Input[i - n] == Input[i + (n + 1)]:
                n += 1

            else:
                done = True

    elif (Input[i] == Input[i + 1] == Input[i - 1]):
        change = True
        single = True
        n = 0

        for x in range(2,((len(Input)-1)/2)):

            if Input[i] == Input[i - x] == Input[i + x]:
                n += 1

if not change:
    print(n)

if change:
    if single:
        print(2*n + 1)
    if double:
        print(2*n + 2)