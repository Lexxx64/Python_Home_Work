def SummaDel(number: int) -> list[int]:
    resultSum = 0
    for i in range(1, number//2 + 1):
        if (number % i == 0):
            resultSum += i
    return resultSum


k = int(input())
for i in range(1, k):
    x = SummaDel(i)
    if SummaDel(x) == i and i != x and k > x:
        print(i, x)