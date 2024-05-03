animal = " chanchito feliz "
print(animal.upper())
print(animal.capitalize())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
# este nos regresa el indice donde se encuentra la palabra
print(animal.find("it"))
print(animal.replace("nch", "abc"))
# esto nos regresa true or false si contiene la palabra dentro de otra palabra
print("nch" in animal)
print("nch" not in animal)
