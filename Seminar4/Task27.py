string = input("Введите строку: ").lower()
words = string.split()
unique_words = {}
for word in words:
    if word in unique_words:
        unique_words[word] += 1
    else:
        unique_words[word] = 1
print(*{len(unique_words)})