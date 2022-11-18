from queue import PriorityQueue
import mapa

'''
    Ana Sofia Schweizer Silvestre
    busca de custo uniforme
'''

mapa, _ = mapa.getMapa() # formando o grafo

partida, chegada = ('Arad', 'Bucharest') # definindo partida e chegada

filaPrioridade = PriorityQueue() # fila de prioridade, a melhor opcao de caminho sempre estará em [0]
visitado = [] # cidades ja visitadas
caminho = [partida] # o caminho ate a chegada
filaPrioridade.put((0, partida, caminho)) # adicionando a cidade de partida a fila de prioridade

while not filaPrioridade.empty():
    custo, no, caminho = filaPrioridade.get() # cidade atual
    if no == chegada: # se cidade atual é a chegada então para loop
        break
    if no not in visitado:
        visitado.append(no)
        vizinhos = mapa.getVizinhos(no) # cidades vizinhas
        for i in vizinhos:
            if i[1] not in visitado: # se proxima cidade ainda não visistada adiciona na fila de prioridade
                moveu = caminho.copy()
                moveu.append(i[1]) # caminho com a proxima cidade
                filaPrioridade.put((custo + i[0], i[1], moveu))
                ''' salva na fila de prioridade com
                        distancia percorrida'''

print(caminho)