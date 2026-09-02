# atv 01 ordem dos lacos
import time
import random

def gerar_matriz(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def multi_ijk(A, B):
    n = len(A)
    C = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

def multi_ikj(A, B):
    n = len(A)
    C = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

n = 50

A = gerar_matriz(n)
B = gerar_matriz(n)

inicio = time.perf_counter()
C1 = multi_ijk(A, B)
tempo_ijk = time.perf_counter() - inicio

inicio = time.perf_counter()
C2 = multi_ikj(A, B)
tempo_ikj = time.perf_counter() - inicio

print(f"Tamanho: {n}x{n}")
print(f"IJK: {tempo_ijk:.4f} segundos")
print(f"IKJ: {tempo_ikj:.4f} segundos")

if tempo_ikj < tempo_ijk:
    fator = tempo_ijk / tempo_ikj
    print(f"IKJ foi {fator:.2f}x mais rápida")
else:
    fator = tempo_ikj / tempo_ijk
    print(f"IJK foi {fator:.2f}x mais rápida")