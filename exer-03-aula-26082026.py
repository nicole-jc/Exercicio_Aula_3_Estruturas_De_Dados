# atv 03 dez linhas escritas
import time
import random
import sys

# matriz normal
def criar_matriz_normal(n, densidade):
    matriz = [[0] * n for _ in range(n)]

    quantidade = int(n * n * densidade)

    for _ in range(quantidade):
        i = random.randrange(n)
        j = random.randrange(n)
        matriz[i][j] = random.randint(1, 100)

    return matriz

def percorrer_matriz_normal(matriz):
    soma = 0

    for linha in matriz:
        for valor in linha:
            if valor != 0:
                soma += valor

    return soma

# matriz esparca
def criar_matriz_esparsa(n, densidade):
    triplas = []

    quantidade = int(n * n * densidade)
    posicoes = set()

    while len(posicoes) < quantidade:
        i = random.randrange(n)
        j = random.randrange(n)
        posicoes.add((i, j))

    for i, j in posicoes:
        valor = random.randint(1, 100)
        triplas.append((i, j, valor))

    return triplas


def percorrer_matriz_esparsa(triplas):
    soma = 0

    for i, j, valor in triplas:
        soma += valor

    return soma

n = 300

densidades = [
    0.01,
    0.05, 
    0.10,
    0.20,
    0.30,
    0.40,
    0.50,
    0.70,
    0.90,
]

print(f"Matriz: {n} x {n}")
print()
print("Densidade | Memória normal | Memória esparsa | Tempo normal | Tempo esparsa")
print("-" * 80)

for densidade in densidades:

    normal = criar_matriz_normal(n, densidade)
    esparsa = criar_matriz_esparsa(n, densidade)

    # medicao memoria
    memoria_normal = sys.getsizeof(normal)

    for linha in normal:
        memoria_normal += sys.getsizeof(linha)

    memoria_esparsa = sys.getsizeof(esparsa)

    for tripla in esparsa:
        memoria_esparsa += sys.getsizeof(tripla)

    # tempo da matriz normal
    inicio = time.perf_counter()
    percorrer_matriz_normal(normal)
    tempo_normal = time.perf_counter() - inicio

    # tempo da matriz esparsa
    inicio = time.perf_counter()
    percorrer_matriz_esparsa(esparsa)
    tempo_esparsa = time.perf_counter() - inicio

    print(
        f"{densidade * 100:8.0f}% | "
        f"{memoria_normal / 1024:10.2f} KB | "
        f"{memoria_esparsa / 1024:10.2f} KB | "
        f"{tempo_normal:.6f} s | "
        f"{tempo_esparsa:.6f} s"
    )