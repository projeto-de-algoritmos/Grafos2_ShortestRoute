import sys
from heapq import heappop, heappush

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(vertices)]

    def adicionar_aresta(self, origem, destino, peso):
        self.grafo[origem].append((destino, peso))
        self.grafo[destino].append((origem, peso))

    def dijkstra(self, origem, destino):
        distancias = [sys.maxsize] * self.vertices
        antecessor = [None] * self.vertices
        visitados = [False] * self.vertices

        heap = [(0, origem)]
        distancias[origem] = 0

        while heap:
            custo, u = heappop(heap)

            if u == destino:
                break

            if visitados[u]:
                continue

            visitados[u] = True

            for v, peso in self.grafo[u]:
                if not visitados[v] and distancias[v] > distancias[u] + peso:
                    distancias[v] = distancias[u] + peso
                    antecessor[v] = u
                    heappush(heap, (distancias[v], v))

        caminho = [destino]

        while caminho[-1] != origem:
            caminho.append(antecessor[caminho[-1]])

        caminho.reverse()

        return distancias[destino], caminho


# Exemplo de uso
if __name__ == "__main__":
    # Criação do grafo
    num_vertices = 8
    grafo = Grafo(num_vertices)

    # Adição das arestas e seus pesos
    grafo.adicionar_aresta(0, 1, 4)
    grafo.adicionar_aresta(0, 2, 2)
    grafo.adicionar_aresta(1, 3, 2)
    grafo.adicionar_aresta(2, 3, 7)
    grafo.adicionar_aresta(2, 4, 3)
    grafo.adicionar_aresta(3, 5, 4)
    grafo.adicionar_aresta(3, 6, 1)

    # Entrada do usuário
    origem = int(input("Digite o ponto de partida: "))
    destino = int(input("Digite o local de destino: "))

    # Cálculo da rota mais rápida
    menor_distancia, rota = grafo.dijkstra(origem, destino)

    # Imprimir o resultado
    print(f"A menor distância entre {origem} e {destino} é {menor_distancia}")
    print("O caminho mais rápido é:", end=" ")
    print(" -> ".join(str(v) for v in rota))