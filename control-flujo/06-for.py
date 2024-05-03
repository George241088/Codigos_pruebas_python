buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", numero)
        break
else:
    print("No se encontro el numero buscado")
