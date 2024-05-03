def suma(*numeros):
    res = 0
    for num in numeros:
        res += num
    print(res)


suma(2, 4, 6)
suma(8, 8)
suma(2, 8, 7, 45, 32)
