# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
print(primer)


segundo = [3, 4, 5]
segundo = set(segundo)

print(segundo)

print(primer | segundo)

# interseccion
print(primer & segundo)

# diferencia
print(primer - segundo)

# diferencia simetrica
print(primer ^ segundo)
