lista = [1, 2, 3, 4]
print(lista)

print(*lista)

lista2 = [5, 6]

combinada = [*lista, *lista2]
print(combinada)


punto1 = {"x": 20}
punto2 = {"y": 30}
nuevopunto = {**punto1, **punto2}

print(nuevopunto)
