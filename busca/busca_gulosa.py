from torch import inverse
import mapa

mapa, distancias = mapa.getMapa()

no, chegada = ('Arad', 'Bucharest') # pontos de partida e chegada
caminho = [no] # caminho percorrido
visitados = [no]

while True:

    vizinhos = mapa.getVizinhos(no) # cidades vizinhas
    distVizinhos = [(distancias[i[1]], i[1]) for i in vizinhos] # pega as distancias heuristicas
    distVizinhos.sort() # ordena para lista de acordo com as distancias euristicas
    for i in distVizinhos:
        if i[1] not in visitados:
            visitados.append(i[1])
            _, no = i # pega a cidade nao visitada com a menor distancia heuristica
            break
    caminho.append(no) # adiciona em caminho
    if no == chegada: # checa se é o destino
        break

print(caminho)