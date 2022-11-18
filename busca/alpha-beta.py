import math

"""
Classe arvore
"""
class arvore:

    def __init__(self, val = None):
        self.valor = val
        self.filhos = []
        self.pai = None
    
    def addFilho(self, valor):
        self.filhos.append(arvore(valor))
        self.filhos[-1].pai = self

def criaArvore():

    no = arvore(3)
    no.addFilho(3)
    no.addFilho(2)
    no.addFilho(2)
    no.filhos[0].addFilho(12)
    no.filhos[0].addFilho(3)
    no.filhos[0].addFilho(8)
    no.filhos[1].addFilho(2)
    no.filhos[1].addFilho(4)
    no.filhos[1].addFilho(6)
    no.filhos[2].addFilho(14)
    no.filhos[2].addFilho(2)
    no.filhos[2].addFilho(7)

    return no

"""
Funcoes auxiliares
"""
def maxArvore(arvore1, arvore2):
    return arvore1 if arvore1.valor > arvore2.valor else arvore2

def minArvore(arvore1, arvore2):
    return arvore2 if arvore1.valor > arvore2.valor else arvore1

"""
Implementacao AlphaBeta
"""
def minimaxDecision(estado):
    v = maxValue(estado, -math.inf, math.inf)
    return v

def maxValue(estado, alpha, beta):
    if estado.filhos == []:
        return estado
    
    v = arvore(-math.inf)
    
    for s in estado.filhos:
        v = maxArvore(v, minValue(s, alpha, beta))

        if v.valor >= beta:
            return v
        
        alpha = max(alpha, v.valor)
    
    return v
    
def minValue(estado, alpha, beta):
    if estado.filhos == []:
        return estado

    v = arvore(math.inf)

    for s in estado.filhos:
        v = minArvore(v, maxValue(s, alpha, beta))

        if v.valor <= alpha:
            return v
        
        beta = min(beta, v.valor)

    return v

no = criaArvore()
print(minimaxDecision(no).valor)