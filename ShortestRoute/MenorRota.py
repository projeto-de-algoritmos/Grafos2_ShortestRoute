import sys
from heapq import heappop, heappush

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(vertices)]
        self.linhas = {}


    def adicionar_aresta(self, origem, destino, peso, linha):
        self.grafo[origem].append((destino, peso))
        self.grafo[destino].append((origem, peso))
        self.linhas[(origem, destino)] = linha
        self.linhas[(destino, origem)] = linha

    def dijkstra(self, origem, destino):
        distancias = [sys.maxsize] * self.vertices
        antecessor = [None] * self.vertices
        visitados = [False] * self.vertices
        linha_atual = {}

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
                    linha_atual[v] = self.linhas[(u, v)]
                    heappush(heap, (distancias[v], v))

        caminho = [destino]
        linha_percurso = []

        while caminho[-1] != origem:
            caminho.append(antecessor[caminho[-1]])
            linha_percurso.append(self.linhas[(caminho[-2], caminho[-1])])

        caminho.reverse()
        linha_percurso.reverse()

        return distancias[destino], caminho, linha_percurso


# Exemplo de uso
if __name__ == "__main__":
    # Criação do grafo
    num_vertices = 8
    grafo = Grafo(num_vertices)
    #Array com os pontos
    pontos = ["Parada UnB Gama", "Parada Faciplac", "Gama Shopping", "Hospital Maria Auxiliadora", "Setor de Industrias", "Vila Olímpica"]

    # Adição das arestas e seus pesos (em minutos)
    grafo.adicionar_aresta(0, 1, 25, "A")
    grafo.adicionar_aresta(2, 0, 25, "B")
    grafo.adicionar_aresta(0, 4, 29, "C")
    grafo.adicionar_aresta(2, 3, 7, "D")
    grafo.adicionar_aresta(2, 4, 3, "E")
    grafo.adicionar_aresta(3, 5, 4, "F")
    grafo.adicionar_aresta(3, 6, 1, "G")

    # Entrada do usuário
    origem = int(input("Digite o ponto de partida: "))
    destino = int(input("Digite o local de destino: "))

    # Cálculo da rota mais rápida 
    menor_distancia, rota, linha_rota = grafo.dijkstra(origem, destino)

    # Imprimir o resultado
    print(f"A menor distância entre {origem} e {destino} é de {menor_distancia} minutos")
    print("A(s) linha(s) a serem usadas é:")
    for i in range(len(rota) - 1):
        linha = linha_rota[i]
        print(f"Linha {linha}")