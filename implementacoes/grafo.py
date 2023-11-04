from vertice_aresta import Vertice, Aresta


class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def get_ordem(self):
        return len(self.vertices)

    def get_tamanho(self):
        return len(self.arestas)

    def vertices(self):
        return self.vertices

    def arestas(self):
        return self.arestas

    # Inserção e remoção de vértices
    def insere_v(self, v: Vertice):
        self.vertices.append(v)

    def cria_e_insere_v(self, id: str, valor: str):
        v = Vertice(id, valor)
        self.insere_v(v)

    def remove_v(self, v: Vertice):
        self.vertices.remove(v)

        for vert_adj in v.adj.keys():
            vert_adj.adj.pop(v)
        
        for arestas in v.adj.values():
            for aresta in arestas:
                self.arestas.remove(aresta)


    # Inserção e remoção de arestas
    def insere_a(self, a: Aresta, u: Vertice, v: Vertice):
        a.incid = (u, v)

        if (u in v.adj) or (v in u.adj):
            u.adj[v].append(a)
            v.adj[u].append(a) if u != v else None
        else:
            u.adj[v] = [a]
            v.adj[u] = [a] if u != v else None

        self.arestas.append(a)

    def cria_e_insere_a(self, id: str, valor: str, u: Vertice, v: Vertice):
        a = Aresta(id, valor)
        self.insere_a(a, u, v)

    def remove_a(self, a):
        self.arestas.remove(a)

        a.incid[0].adj[a.incid[1]].remove(a)
        a.incid[0].adj.pop(a.incid[1]) if len(a.incid[0].adj[a.incid[1]]) == 0 else None

        if a.incid[0] != a.incid[1]:
            a.incid[1].adj[a.incid[0]].remove(a)
            a.incid[1].adj.pop(a.incid[0]) if len(a.incid[1].adj[a.incid[0]]) == 0 else None

    # Iterável de adjacência
    def adj(self, v: Vertice):
        return v.adj.keys()

    # Aresta a partir de dois vértices
    def get_a(self, u: Vertice, v: Vertice) -> list | None:
        return u.adj[v] if v in u.adj else None

    # Grau
    def grau(self, v: Vertice):
        return len(v.adj)

    # Incidência
    def vertices_a(self, a: Aresta):
        return a.incid

    def oposto(self, v: Vertice, a: Aresta):
        return a.incid[(a.incid.index(v) + 1) % 2]


from vertice_aresta import VerticeDirigido, ArestaDirigida

class Digrafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def get_ordem(self):
        return len(self.vertices)

    def get_tamanho(self):
        return len(self.arestas)

    def vertices(self):
        return self.vertices

    def arestas(self):
        return self.arestas

    # Inserção e remoção de vértices
    def insere_v(self, v: Vertice):
        self.vertices.append(v)

    def cria_e_insere_v(self, id: str, valor: str):
        v = VerticeDirigido(id, valor)
        self.insere_v(v)

    def remove_v(self, v: VerticeDirigido):
        self.vertices.remove(v)

        for vert_suc in v.suc.keys():
            vert_suc.ant.pop(v)

        for vert_ant in v.ant.keys():
            vert_ant.suc.pop(v)

        for arestas_saida in v.suc.values():
            for aresta_saida in arestas_saida:
                self.arestas.remove(aresta_saida)

        for arestas_entrada in v.suc.values():
            for aresta_entrada in arestas_entrada:
                self.arestas.remove(aresta_entrada)

    # Inserção e remoção de arestas
    def insere_a(self, a: ArestaDirigida, u: VerticeDirigido, v: VerticeDirigido):
        a.incid = (u, v)

        if (u in v.ant) or (v in u.suc):
            u.suc[v].append(a)
            v.ant[u].append(a)
        else:
            u.suc[v] = [a]
            v.ant[u] = [a]

        self.arestas.append(a)

    def cria_e_insere_a(self, id: str, valor: str, u: VerticeDirigido, v: VerticeDirigido):
        a = ArestaDirigida(id, valor)
        self.insere_a(a, u, v)

    def remove_a(self, a):
        self.arestas.remove(a)

        a.incid[0].suc[a.incid[1]].remove(a)
        a.incid[0].suc.pop(a.incid[1]) if len(a.incid[0].suc[a.incid[1]]) == 0 else None

        a.incid[1].ant[a.incid[0]].remove(a)
        a.incid[1].ant.pop(a.incid[0]) if len(a.incid[1].suc[a.incid[0]]) == 0 else None

        a.incid[0].adj[a.incid[1]].remove(a)
        if len(a.incid[0].adj[a.incid[1]]) == 0:
            a.incid[0].adj.pop(a.incid[1])

        if a.incid[0] != a.incid[1]:
            a.incid[1].adj[a.incid[0]].remove(a)
            if len(a.incid[1].adj[a.incid[0]]) == 0:
                a.incid[1].adj.pop(a.incid[0])

    # Iterável de adjacência
    def adj(self, v: VerticeDirigido):
        return v.adj.keys()

    # Aresta a partir de dois vértices
    def get_a(self, u: VerticeDirigido, v: VerticeDirigido) -> list | None:
        return u.adj[v] if v in u.adj else None

    # Grau
    def grau(self, v: VerticeDirigido):
        return len(v.adj)

    # Incidência
    def vertices_a(self, a: ArestaDirigida):
        return a.incid

    def oposto(self, v: VerticeDirigido, a: ArestaDirigida):
        return a.incid[(a.incid.index(v) + 1) % 2]

def main():
    g = Grafo()
    g.cria_e_insere_v('v1', 'vA')
    g.cria_e_insere_v('v2', 'vB')
    g.cria_e_insere_v('v3', 'vC')
    g.cria_e_insere_v('v4', 'vD')
    g.cria_e_insere_v('v5', 'vE')
    g.cria_e_insere_a('a1', 'aA', g.vertices[0], g.vertices[1])
    g.cria_e_insere_a('a2', 'aB', g.vertices[0], g.vertices[3])
    g.cria_e_insere_a('a3', 'aC', g.vertices[1], g.vertices[3])
    g.cria_e_insere_a('a4', 'aD', g.vertices[3], g.vertices[0])
    g.cria_e_insere_a('a5', 'aE', g.vertices[3], g.vertices[4])
    g.cria_e_insere_a('a6', 'aF', g.vertices[3], g.vertices[4])
    
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