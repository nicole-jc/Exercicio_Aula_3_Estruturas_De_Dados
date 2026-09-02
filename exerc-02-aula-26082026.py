# atv 02 matriz esparca
class MatrizEsparsa:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.triplas = []

    def escrever(self, linha, coluna, valor):
        for i, (l, c, v) in enumerate(self.triplas):
            if l == linha and c == coluna:

                if valor == 0:
                    self.triplas.pop(i)
                else:
                    self.triplas[i] = (linha, coluna, valor)

                return
            
        if valor != 0:
            self.triplas.append((linha, coluna, valor))

    def ler(self, linha, coluna):
        for l, c, v in self.triplas:
            if l == linha and c == coluna:
                return v

        return 0

    def percorrer_nao_nulos(self):
        for linha, coluna, valor in self.triplas:
            print(f"({linha}, {coluna}) = {valor}")


matriz = MatrizEsparsa(5, 5)

matriz.escrever(0, 1, 10)
matriz.escrever(1, 3, 20)
matriz.escrever(3, 2, 30)
matriz.escrever(4, 4, 40)

print("Valor [1][3]:", matriz.ler(1, 3))
print("Valor [2][2]:", matriz.ler(2, 2))

print("\nElementos não nulos:")
matriz.percorrer_nao_nulos()