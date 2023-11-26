from vertice_aresta import Vertice, Aresta

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def get_ordem(self) -> int:
        return len(self.vertices)

    def get_tamanho(self) -> int:
        return len(self.arestas)

    def vertices(self) -> list:
        return self.vertices

    def arestas(self) -> list:
        return self.arestas

    # Inserção e remoção de vértices
    def insere_v(self, v: Vertice) -> None:
        self.vertices.append(v)

    def cria_e_insere_v(self, id: str) -> None:
        v = Vertice(id)
        self.insere_v(v)

    def remove_v(self, v: Vertice) -> None:
        self.vertices.remove(v)

        for vert_adj in v.adj.keys():
            vert_adj.adj.pop(v)
        
        for arestas in v.adj.values():
            for aresta in arestas:
                self.arestas.remove(aresta)


    # Inserção e remoção de arestas
    def insere_a(self, a: Aresta, u: Vertice, v: Vertice) -> None:
        a.incid = (u, v)

        if (u in v.adj) or (v in u.adj):
            u.adj[v].append(a)
            v.adj[u].append(a) if u != v else None
        else:
            u.adj[v] = [a]
            v.adj[u] = [a] if u != v else None

        self.arestas.append(a)

    def cria_e_insere_a(self, id: str, u: Vertice, v: Vertice) -> None:
        a = Aresta(id)
        self.insere_a(a, u, v)

    def remove_a(self, a) -> None:
        self.arestas.remove(a)

        a.incid[0].adj[a.incid[1]].remove(a)
        a.incid[0].adj.pop(a.incid[1]) if len(a.incid[0].adj[a.incid[1]]) == 0 else None

        if a.incid[0] != a.incid[1]:
            a.incid[1].adj[a.incid[0]].remove(a)
            a.incid[1].adj.pop(a.incid[0]) if len(a.incid[1].adj[a.incid[0]]) == 0 else None

    # Iterável de adjacência
    def adj(self, v: Vertice) -> set:
        return v.adj.keys()

    # Aresta a partir de dois vértices
    def get_a(self, u: Vertice, v: Vertice) -> list | None:
        return u.adj[v] if v in u.adj else None

    # Grau
    def grau(self, v: Vertice) -> int:
        return len(v.adj)

    # Incidência
    def vertices_a(self, a: Aresta) -> tuple:
        return a.incid

    def oposto(self, v: Vertice, a: Aresta) -> Vertice:
        return a.incid[(a.incid.index(v) + 1) % 2]


def main():
    g = Grafo()
    g.cria_e_insere_v('v1')
    g.cria_e_insere_v('v2')
    g.cria_e_insere_v('v3')
    g.cria_e_insere_v('v4')
    g.cria_e_insere_v('v5')
    g.cria_e_insere_a('a1', g.vertices[0], g.vertices[1])
    g.cria_e_insere_a('a2', g.vertices[0], g.vertices[3])
    g.cria_e_insere_a('a3', g.vertices[1], g.vertices[3])
    g.cria_e_insere_a('a4', g.vertices[3], g.vertices[0])
    g.cria_e_insere_a('a5', g.vertices[3], g.vertices[4])
    g.cria_e_insere_a('a6', g.vertices[3], g.vertices[4])
    
    # Teste 1
    # for vert in g.vertices:
    #     print(vert)
    # for aresta in g.arestas:
    #     print(aresta) 

    # Teste 2
    # for vert in g.vertices:
    #     for chave in vert.adj.keys():
    #         print(vert, chave)
    # print('=================')
    # g.remove_a(g.arestas[2])
    # for vert in g.vertices:
    #     for chave in vert.adj.keys():
    #         print(vert, chave)

    # Teste 3
    # for aresta in g.arestas:
    #     print(aresta)
    # print('=================')
    # g.remove_v(g.vertices[1])
    # for aresta in g.arestas:
    #     print(aresta)

    # Teste 4
    # for vert_adj in g.adj(g.vertices[3]):
    #     print(vert_adj)
    # print('=================')
    # g.remove_a(g.arestas[2])
    # for vert_adj in g.adj(g.vertices[3]):
    #     print(vert_adj)

    # Teste 5
    # for v in g.vertices:
    #     print(g.grau(v))
    # print('=================')
    # g.remove_a(g.arestas[2])
    # for v in g.vertices:
    #     print(g.grau(v))

    # Teste 6
    # print(g.get_a(g.vertices[0], g.vertices[3]))
    # print(g.get_a(g.vertices[3], g.vertices[0]))

    # Teste 7
    # print(g.oposto(g.vertices[0], g.arestas[1]))
    # print(g.oposto(g.vertices[3], g.arestas[1]))

if __name__=='__main__':
    main()