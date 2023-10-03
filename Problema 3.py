def elemento_mayor(vector):
    max_valor = max(vector)
    max_posicion = vector.index(max_valor)
    return max_posicion, max_valor

vector_3 = [5, 10, 8, 3, 20, 15, 7, 2, 9, 18, 12, 6, 25, 14, 1, 4, 11, 19, 13, 16, 21, 22, 17, 24, 23, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
posicion, valor = elemento_mayor(vector_3)
print(f"El elemento mayor está en la posición {posicion} y su valor es {valor}")
