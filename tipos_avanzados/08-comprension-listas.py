usuarios = [["chanchito", 2], ["Felipe", 1], ["Pulga", 5]]

# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filtrar

nombres = [usuario for usuario in usuarios if usuario[1] > 1]
print(nombres)

# filtrada y transformada
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 1]
print(nombres)

# transformar -> usando lambda = map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# filtrat -> usando lambda = filter
menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosusuarios)
