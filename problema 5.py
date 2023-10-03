def analizar_numeros(vector):
    ceros = vector.count(0)
    negativos = len([x for x in vector if x < 0])
    positivos = len([x for x in vector if x > 0])
    suma_negativos = sum([x for x in vector if x < 0])
    suma_positivos = sum([x for x in vector if x > 0])
    return ceros, negativos, positivos, suma_negativos, suma_positivos

vector_5 = [0, 1, -2, 3, -4, 5, 0, -6, 7, -8, 9, 10, -11, 12, 13, -14, 15, 0, -16, 17, 18, -19, 20, 21, 22, -23, 24, 0, -25]
ceros, negativos, positivos, suma_negativos, suma_positivos = analizar_numeros(vector_5)
print(f"Números ceros: {ceros}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")
print(f"Suma de negativos: {suma_negativos}")
print(f"Suma de positivos: {suma_positivos}")
