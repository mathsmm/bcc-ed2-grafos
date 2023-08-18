from matriz import Matriz


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
        self.vertices = list()
        self.arestas  = list()
        self.mtz_adj  = Matriz()

    def get_ordem(self):
        return len(self.vertices)

    def get_tamanho(self):
        return len(self.arestas)

    def vertices(self):
        return self.vertices

    def arestas(self):
        return self.arestas

    def insere_v(self, v: Vertice):
        self.vertices.append(v)

    def cria_e_insere_v(self, id: str, valor: str):
        v = Vertice(id, valor)
        self.insere_v(v)

    def remove_v(self, v: Vertice):
        self.remove_v_pelo_indice(self.vertices.index(v))

    # O(n^2), n == qtd vértices no grafo
    def remove_v_pelo_indice(self, v_idx: int):
        i = 0
        len_vertices = self.get_ordem()

        # Remove todas as adjacências relacionadas ao vértice
        while i < len_vertices:
            if  self.mtz_adj.get((v_idx, i)) != None:
                self.mtz_adj.pop((v_idx, i))
            if  self.mtz_adj.get((i, v_idx)) != None:
                self.mtz_adj.pop((i, v_idx))
            i += 1

        # Na matriz de adjacência, decrementa o índice de todos 
        # os vértices posteriores ao que se deseja remover
        # ANOTAÇÃO: TEM COMO MELHORAR USANDO ITERAÇÃO SOBRE O DICIONÁRIO
        i = v_idx + 1
        while i < len_vertices:
            j = v_idx + 1
            while j < len_vertices:
                if  self.mtz_adj.get((i, j)) != None:
                    self.mtz_adj[(i - 1, j - 1)] = self.mtz_adj.pop((i, j))
                if  self.mtz_adj.get((j, i)) != None:
                    self.mtz_adj[(j - 1, i - 1)] = self.mtz_adj.pop((j, i))
                j += 1
            i += 1

        for key, value in self.mtz_adj:
            # key   == (i, j)
            # value == [a1...an]
            if v_idx in key:
                self.mtz_adj.pop(key)
                continue



        # Remove o vértice da lista de vértices
        self.vertices[v_idx].pop(v_idx)

def main():
    pass

if __name__ == '__main__':
    main()