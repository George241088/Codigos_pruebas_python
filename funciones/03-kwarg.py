def get_product(**datos):
    print(datos)
    print(datos["name"], datos["desc"])


get_product(id="id", name="iphone", desc="Esto es un iphone")
