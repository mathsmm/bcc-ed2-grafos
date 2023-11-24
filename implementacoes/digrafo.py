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
    def insere_v(self, v: VerticeDirigido):
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

    def remove_a(self, a: ArestaDirigida):
        self.arestas.remove(a)

        a.incid[0].suc[a.incid[1]].remove(a)
        a.incid[0].suc.pop(a.incid[1]) if len(a.incid[0].suc[a.incid[1]]) == 0 else None

        a.incid[1].ant[a.incid[0]].remove(a)
        a.incid[1].ant.pop(a.incid[0]) if len(a.incid[1].suc[a.incid[0]]) == 0 else None

        # a.incid[0].adj[a.incid[1]].remove(a)
        # if len(a.incid[0].adj[a.incid[1]]) == 0:
        #     a.incid[0].adj.pop(a.incid[1])

        # if a.incid[0] != a.incid[1]:
        #     a.incid[1].adj[a.incid[0]].remove(a)
        #     if len(a.incid[1].adj[a.incid[0]]) == 0:
        #         a.incid[1].adj.pop(a.incid[0])

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