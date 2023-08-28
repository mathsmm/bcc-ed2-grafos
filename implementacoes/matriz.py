class MatrizAdjacencia:
    def __init__(self):
        """
        Inicializa uma matriz de adjacência tridimensional 
        (matriz de listas) com 1 linha e 0 colunas
        """
        self.mtz = [[]]

    def __getitem__(self, key: int):
        return self.mtz[key]

    def __str__(self):
        s = ''
        i = 0
        while i < len(self.mtz):
            s += '('
            j = 0
            while j < len(self.mtz[i]):
                s += f' {self.mtz[i][j]}'
                j += 1
            s += ' )\n'
            i += 1
        return s

    def add_lin(self, qtd_lin: int) -> None:
        i = 0
        while i < qtd_lin:
            self.mtz.append([] * len(self.mtz[0]))
            i += 1

    def add_col(self, qtd_col: int) -> None:
        for lin in self.mtz:
            j = 0
            while j < qtd_col:
                lin.append([])
                j += 1

    def pop_lin(self, ind_lin: int) -> list:
        return self.mtz.pop(ind_lin)

    def pop_col(self, ind_col: int) -> list:
        l = []
        for lin in self.mtz:
            l.append(lin.pop(ind_col))
        return l


mtz = MatrizAdjacencia()

mtz.add_lin(2)
mtz.add_col(3)
mtz[0][0].append(1)
mtz[0][1].append(2)
mtz[0][2].append(3)
mtz[1][0].append(4)
mtz[1][1].append(5)
mtz[1][2].append(6)
mtz[2][0].append(7)
mtz[2][1].append(8)
mtz[2][2].append(9)
mtz.pop_col(1)
mtz.pop_lin(1)
print(mtz)