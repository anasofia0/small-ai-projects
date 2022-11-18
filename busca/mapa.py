from grafo import *

'''
    Obtendo os dados e construindo o grafo
'''
def getMapa():
    distancias = {}
    mapa = Grafo()

    with(open('cidades.txt')) as cidades:
        
        for linha in cidades.readlines():
            cidade, dist = linha[:-1].split(', ')
            mapa.addVertice(cidade)
            distancias[cidade] = int(dist)

    with(open('estradas.txt')) as estradas:

        for linha in estradas.readlines():
            cidade1, cidade2, dist = linha[:-1].split(', ')
            mapa.addAresta(cidade1, cidade2, int(dist))
    
    return mapa, distancias
