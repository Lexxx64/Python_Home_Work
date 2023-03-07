def get_exponentiation(num, power):
    if power == 0 or num == 0 or num == 1:
        return 1
    return (num * get_exponentiation(num, power - 1))


print(get_exponentiation(int(input('число: ')), int(input('степень: '))))
