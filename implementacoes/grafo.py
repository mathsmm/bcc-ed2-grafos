from matriz import MatrizAdjacencia


class Vertice:
    def __init__(self, id: str, valor: str):
        self.id = id
        self.valor = valor

class Aresta:
    def __init__(self, id: str, valor: str):
        self.id = id
        self.valor = valor

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas  = []
        self.mtz_adj  = MatrizAdjacencia()

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

    def cria_e_insere_v(self, id: str, valor: str) -> None:
        v = Vertice(id, valor)
        self.insere_v(v)

    def remove_v(self, v: Vertice) -> None:
        self.remove_v_pelo_indice(self.vertices.index(v))

    def remove_v_pelo_indice(self, v_ind: int) -> None:
        self.mtz_adj.pop_lin(v_ind)
        self.mtz_adj.pop_col(v_ind)
        self.vertices.pop(v_ind)

    # Inserção e remoção de arestas
    def cria_e_insere_a(self, id: str, valor: str, u: Vertice, v: Vertice) -> None:
        a = Aresta(id, valor)
        self.insere_a(a, self.vertices.index(u), self.vertices.index(v))

    def cria_e_insere_a(self, id: str, valor: str, u_ind: int, v_ind: int) -> None:
        a = Aresta(id, valor)
        self.insere_a(a, u_ind, v_ind)

    def insere_a(self, a: Aresta, u: Vertice, v: Vertice) -> None:
        self.insere_a(a, self.vertices.index(u), self.vertices.index(v))

    def insere_a_pelos_indices(self, a: Aresta, u_ind: int, v_ind: int) -> None:
        a_ind = self.get_tamanho()
        self.arestas.append(a)
        self.mtz_adj[u_ind][v_ind].append(a_ind)

    def remove_a(self, a: Aresta) -> None:
        self.remove_a_pelo_indice(self.arestas.index(a))

    def remove_a_pelo_indice(self, a_ind: int) -> None:
        for lin in self.mtz_adj:
            for col in lin:
                i = 0
                while i < len(col):
                    if col[i] == a_ind:
                        col.pop(a_ind)
                    elif col[i] > a_ind:
                        col[i] -= 1
                        i += 1
        self.arestas.pop(a_ind)

    def adj(self, v: Vertice) -> set:
        return self.adj_pelo_indice(self.vertices.index(v))

    def adj_pelo_indice(self, v_ind: int) -> set:
        l = set()
        i = 0
        ordem = self.get_ordem()
        while i < ordem:
            if len(self.mtz_adj[v_ind][i]) > 0 or len(self.mtz_adj[i][v_ind]) > 0:
                l.add(self.vertices[i])
            i += 1
        return l

    def get_a(self, u: Vertice, v: Vertice):
        return self.get_a_pelos_indices(self.vertices.index(u), self.vertices.index(v))

    def get_a_pelos_indices(self, u_ind: int, v_ind: int):
        pass


def main():
    pass

if __name__ == '__main__':
    main()