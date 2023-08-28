class Vertice:
    def __init__(self, id: str, valor: str):
        self.id = id
        self.valor = valor
        self.sucessores = set()
        self.antecessores = set()

    def __str__(self):
        return f'({self.id}: {self.valor})'

class Aresta:
    def __init__(self, id: str, valor: str, u: Vertice, v: Vertice):
        self.id = id
        self.valor = valor
        self.incid = (u, v)

    def __str__(self):
        return f'<{self.id} ({self.incid[0].id} -> {self.incid[1].id}): {self.valor}>'

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
    def cria_e_insere_v(self, id: str, valor: str):
        v = Vertice(id, valor)
        self.insere_v(v)

    def insere_v(self, v: Vertice):
        self.vertices.append(v)

    def remove_v(self, v: Vertice):
        for vert in self.vertices:
            vert.sucessores.discard(v)
            vert.antecessores.discard(v)

        i = 0
        tamanho = self.get_tamanho()
        while i < tamanho:
            a = self.arestas[i]
            print(a)
            if v in a.incid:
                self.arestas.remove(a)
                tamanho -= 1
                continue
            i += 1

        self.vertices.remove(v)

    # Inserção e remoção de arestas
    def cria_e_insere_a(self, id: str, valor: str, u: Vertice, v: Vertice):
        a = Aresta(id, valor, u, v)
        u.sucessores.add(v)
        v.antecessores.add(u)
        self.arestas.append(a)

    def insere_a(self, a: Aresta, u: Vertice, v: Vertice):
        a.incid = (u, v)
        u.sucessores.add(v)
        v.antecessores.add(u)
        self.arestas.append(a)

    def remove_a(self, a):
        self.arestas.remove(a)
        for aresta in self.arestas:
            if aresta.incid == a.incid and aresta != a:
                return
        a.incid[0].sucessores.discard(a.incid[1])
        a.incid[1].antecessores.discard(a.incid[0])

    # Iteráveis de adjacência
    def adj(self, v: Vertice):
        return v.antecessores.union(v.sucessores)

    def suc(v: Vertice):
        return v.sucessores

    def ant(v: Vertice):
        return v.antecessores

    # Aresta a partir de dois vértices
    def get_a(self, u: Vertice, v: Vertice):
        for aresta in self.arestas:
            if aresta.incid == (u, v):
                return aresta
        return None

    # Graus
    def grau_e(v: Vertice):
        return len(v.antecessores)

    def grau_s(v: Vertice):
        return len(v.sucessores)

    # Incidência
    def vertices_a(a: Aresta):
        return a.incid

    def oposto(v: Vertice, a: Aresta):
        if a.incid[0] == v:
            return a.incid[1]
        elif a.incid[1] == v:
            return a.incid[0]
        else:
            return None

    # Iteráveis de arestas
    def arestas_e(self, v: Vertice):
        l = set()
        for aresta in self.arestas:
            l.add(aresta) if aresta.incid[1] == v else None
        return l

    def arestas_s(self, v: Vertice):
        l = set()
        for aresta in self.arestas:
            l.add(aresta) if aresta.incid[0] == v else None
        return l

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
    
    # for aresta in g.arestas:
    #     print(aresta)
    
    g.remove_v(g.vertices[0])

    print('======================')
    for aresta in g.arestas:
        print(aresta)

    # s = g.adj(g.vertices[4])
    # for val in s:
    #     print(val)

if __name__=='__main__':
    main()