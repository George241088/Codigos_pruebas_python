punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])


# agregar elemento a punto
punto["z"] = 70

print(punto)


# verificar si una llave esta dentro del diccionario
if "lala" in punto:
    print("Se encontro el elemento lala", punto["lala"])


print(punto.get("x"))
print(punto.get("lala", 97))


usuarios = [
    {"id": 1, "nombre": "Jorge", "ap": "valdes"},
    {"id": 2, "nombre": "Alejandra", "ap": "Galicia"},
    {"id": 3, "nombre": "Melissa", "ap": "Ortiz"}
]

for usuario in usuarios:
    print(usuario["nombre"])
