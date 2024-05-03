def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    nueva_palabra = ""
    for num in range(len(texto)):
        pos = len(texto) - num
        letra = texto[pos - 1]
        nueva_palabra = nueva_palabra + letra
    if (texto == nueva_palabra):
        return True
    else:
        return False


print("reconocer", es_palindromo("reconocer"))
print("Abba", es_palindromo("Abba"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))
