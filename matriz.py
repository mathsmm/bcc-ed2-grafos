class Matriz:
    def __init__(self):
        """Inicializa uma matriz com 1 linha e 0 colunas"""
        self.mtz = [[]]

    def __getitem__(self, key: int):
        return self.mtz[key]

    def __str__(self):
        s = ''
        i = 0
        while i < len(self.mtz):
            s += '['
            j = 0
            while j < len(self.mtz[i]):
                s += f' {self.mtz[i][j]}'
                j += 1
            s += ' ]\n'
            i += 1
        return s
    
    def add_lin(self, qtd_lin: int) -> None:
        i = 0
        while i < qtd_lin:
            self.mtz.append([0] * len(self.mtz[0]))
            i += 1

    def add_col(self, qtd_col: int) -> None:
        for i in self.mtz:
            j = 0
            while j < qtd_col:
                i.append(0)
                j += 1

    def pop_lin(self) -> tuple:
        pass

    def pop_col(self) -> tuple:
        pass

mtz = Matriz()

mtz.add_lin(2)
mtz.add_col(3)
print(mtz)