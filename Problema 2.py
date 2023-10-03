def sumar_vectores(A, B):
    C = [a + b for a, b in zip(A, B)]
    return C

vector_A = [1] * 36  
vector_B = [2] * 36  
vector_C = sumar_vectores(vector_A, vector_B)
print(vector_C)
