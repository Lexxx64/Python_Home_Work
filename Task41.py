list1 = list(map(int, input().split()))
n = len(list1)
count = 0

for i in range(1, n - 1):
    if list1[i-1] < list1[i] > list1[i+1]:
        count += 1
print(count)
