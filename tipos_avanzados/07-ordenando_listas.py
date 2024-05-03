numeros = [12, 53, 1, 567, 89, 3, 45, 67, 35, 26, 95, 834, 534]

print(numeros)
numeros.sort(reverse=True)
print(numeros)

# numeros2 = sorted(numeros)
numeros2 = sorted(numeros, reverse=True)

print(numeros2)


usuarios = [["chanchito", 2], ["Felipe", 1], ["Pulga", 5]]


# def ordena(elemento):
#     return elemento[1]


usuarios.sort(key=lambda parametros: parametros[1])
print(usuarios)
