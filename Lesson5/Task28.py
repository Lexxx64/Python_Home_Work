def get_sum(num, num_2):
    if num_2 == 0:
        return num
    return get_sum(num + 1, num_2 - 1)


print(get_sum(int(input('число 1: ')), int(input('Число 2: '))))
