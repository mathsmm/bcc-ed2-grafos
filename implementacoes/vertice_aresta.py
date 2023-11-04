class Vertice:
    def __init__(self, id: str, valor: str):
        self.id = id
        self.valor = valor
        self.adj = dict() # Adjacentes

    def __str__(self):
        return f'<{self.id}: {self.valor}>'

class Aresta:
    def __init__(self, id: str, valor: str):
        self.id = id
        self.valor = valor
        self.incid = tuple()

    def __str__(self):
        return f'<({self.incid[0].id} -- {self.incid[1].id}) {self.id}: {self.valor}>'

class VerticeDirigido:
    def __init__(self, id: str, valor: str):
        self.id = id
        self.valor = valor
        self.suc = dict() # Sucessores
        self.ant = dict() # Antecessores

    def __str__(self):
        return f'<{self.id}: {self.valor}>'

class ArestaDirigida:
    def __init__(self, id: str, valor: str):
        self.id = id
        self.valor = valor
        self.incid = tuple()

    def __str__(self):
        return f'<({self.incid[0].id} -> {self.incid[1].id}) {self.id}: {self.valor}>'