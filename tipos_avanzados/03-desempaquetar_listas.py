numeros = [1, 2, 3]

# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

primero, *otros = numeros
print(primero, otros)

numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prim, seg, *otros, penultimo, ultimo = numeros2
print(prim, seg, otros, penultimo, ultimo)
