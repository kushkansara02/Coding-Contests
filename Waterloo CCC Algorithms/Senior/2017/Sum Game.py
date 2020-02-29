# Sum Game

N = int(input())
swifts = input().split()
semaphores = input().split()

# def SumUpTillK(k, team):
#     sum = 0
#
#     for i in range(k + 1):
#         sum += int(team[i])
#
#     return sum
#
# answer = 0
#
# for i in range(N - 1, -1, -1):
#     if SumUpTillK(i, swifts) == SumUpTillK(i, semaphores):
#         answer = i + 1
#         break
#
# print(answer)

swiftsSum = [int(swifts[0])]
semaphoresSum = [int(semaphores[0])]

for i in range(1, N):
    swiftsSum.append(int(swiftsSum[i - 1]) + int(swifts[i]))
    semaphoresSum.append(int(semaphoresSum[i - 1]) + int(semaphores[i]))

answer = 0

for i in range(N - 1, -1, -1):
    if swiftsSum[i] == semaphoresSum[i]:
        answer = i + 1
        break

print(answer)