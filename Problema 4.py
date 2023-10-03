def elevar_al_cuadrado(vector):
    resultado = [x**2 for x in vector]
    return resultado

vector_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
resultado = elevar_al_cuadrado(vector_4)
print(f"Vector original: {vector_4}")
print(f"Vector resultante: {resultado}")
