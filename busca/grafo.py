class Grafo:
    def __init__(self):
        self.vizinhos = []
        self.nome = []
        self.peso = {}

    def __len__(self):
        return len(self.nomes)

    def __getitem__(self, nome):
        return [self.nome[i] for i in self.vizinhos[self.nome.index(nome)]]

    def addVertice(self, nome):
        if nome not in self.nome:
            self.nome.append(nome)
            self.vizinhos.append([])
            self.peso[nome] = {}

    def addAresta(self, nome1, nome2, peso=None):
        vert1 = self.nome.index(nome1)
        vert2 = self.nome.index(nome2)
        self.vizinhos[vert1].append(vert2)
        self.vizinhos[vert2].append(vert1)

        self.peso[nome1][nome2] = peso
        self.peso[nome2][nome1] = peso

    def getVizinhos(self, nome):
        return [(self.peso[nome][i], i) for i in self.peso[nome]]