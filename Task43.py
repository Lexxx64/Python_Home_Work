list1 = list(map(int, input().split()))
n = len(list1)
count = 0

for i in range(n):
    for j in range(i, n):
        if i != j and list1[i] == list1[j]:
            count += 1
print(count)
