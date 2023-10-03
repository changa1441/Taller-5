def promedio_y_mayores(vector):
    suma = sum(vector)
    promedio = suma / len(vector)
    mayores = [x for x in vector if x > promedio]
    return promedio, len(mayores), mayores

vector_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
            210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390]
prom, cant_mayores, lista_mayores = promedio_y_mayores(vector_1)
print(f"Promedio: {prom}")
print(f"Número de datos mayores que el promedio: {cant_mayores}")
print(f"Lista de valores mayores que el promedio: {lista_mayores}")
