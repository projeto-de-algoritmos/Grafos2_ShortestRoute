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
    num_vertices = 2000
    grafo = Grafo(num_vertices)


    # Adição das arestas e seus pesos (em minutos)
    # Ponto de partida/ destino / tempo/ linha de ônibus

    grafo.adicionar_aresta(1001, 1002, 3, "3210")
    grafo.adicionar_aresta(1002, 1003, 4, "3210")
    grafo.adicionar_aresta(1003, 1004, 2, "3210")
    grafo.adicionar_aresta(1004, 1005, 3, "3210")   
    grafo.adicionar_aresta(1005, 1006, 5, "3210")
    grafo.adicionar_aresta(1006, 1007, 2, "3210")
    grafo.adicionar_aresta(1007, 1008, 3, "3210")
    grafo.adicionar_aresta(1008, 1009, 2, "3210")
    grafo.adicionar_aresta(1009, 1010, 3, "3210")
    grafo.adicionar_aresta(1010, 1011, 4, "3210")
    grafo.adicionar_aresta(1011, 1012, 3, "3210")
    grafo.adicionar_aresta(1012, 1013, 2, "3210")   
    grafo.adicionar_aresta(1013, 1014, 1, "3210")
    grafo.adicionar_aresta(1014, 1015, 3, "3210")
    grafo.adicionar_aresta(1015, 1016, 4, "3210")
    grafo.adicionar_aresta(1016, 1017, 2, "3210")
    grafo.adicionar_aresta(1017, 1018, 1, "3210")
    grafo.adicionar_aresta(1018, 1019, 2, "3210")


    grafo.adicionar_aresta(1020, 1021, 2, "2063")
    grafo.adicionar_aresta(1021, 1022, 3, "2063")
    grafo.adicionar_aresta(1022, 1011, 2, "2063")
    grafo.adicionar_aresta(1011, 1023, 3, "2063")   
    grafo.adicionar_aresta(1023, 1024, 3, "2063")
    grafo.adicionar_aresta(1024, 1004, 1, "2063")
    grafo.adicionar_aresta(1004, 1025, 2, "2063")
    grafo.adicionar_aresta(1025, 1017, 3, "2063")
    grafo.adicionar_aresta(1017, 1027, 2, "2063")
  

    grafo.adicionar_aresta(1028, 1029, 3, "3204")
    grafo.adicionar_aresta(1029, 1030, 2, "3204")
    grafo.adicionar_aresta(1030, 1031, 3, "3204")
    grafo.adicionar_aresta(1031, 1004, 4, "3204")   
    grafo.adicionar_aresta(1004, 1005, 3, "3204")
    grafo.adicionar_aresta(1005, 1003, 2, "3204")
    grafo.adicionar_aresta(1003, 1027, 5, "3204")
    grafo.adicionar_aresta(1027, 1003, 2, "3204")
    grafo.adicionar_aresta(1003, 1018, 1, "3204")
    grafo.adicionar_aresta(1018, 1003, 3, "3204")


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
        destino = rota[i]
        print(f"Linha {linha} no ponto {destino}")