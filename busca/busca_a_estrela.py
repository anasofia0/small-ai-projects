import mapa

def emListaAberto(aberto, no):

    for a in range(len(aberto)):
        if no == aberto[a][2]:
            return (a, True)
    else:
        return (-1, False)

mapa, distancias = mapa.getMapa()

inicio, chegada = ('Arad', 'Bucharest')

aberto = [] # lista com as cidades candidatatas ao caminho
fechado = [] # lista com as cidades que não são mais candidatas
caminho = [inicio] # caminho
custoG = {inicio: 0} # custo com os valores do custo de movimentação
aberto.append((distancias[inicio], inicio, caminho)) # adiciona o ponto inicial a aberto
encontrada = False

while aberto != []: # enquanto aberto não for vazio

    index = aberto.index(min(aberto))
    f, no, caminho = aberto[index] # candidato que tem o menor custo f, sendo f = custo g + distazncia heuristica até destino
    if no == chegada: # checa se candidato nó é o destino
        break
    
    aberto.pop(index) # tira o candidato de aberto
    fechado.append(no) # e o adiciona a fechado
    vizinhos = mapa.getVizinhos(no)
    for i in vizinhos: # para cada vizinho de candidato
        if i[1] in fechado: # se vizinho está em fechado então pula para próximo vizinho
            continue
        custo = custoG[no] + i[0] #  novo custo g = g(candidato) + distancia até vizinho
            
        index, existe = emListaAberto(aberto, i[1])
        if existe and custo < custoG[i[1]]: # se vizinho está em aberto e o novo custo g é menor que o seu custo registrado
            aberto.pop(index) # tira vizinho de aberto
        if not existe and i[1] not in fechado: # se não esta em aberto e nem em fechado
            aberto.append((custo + distancias[i[1]], i[1], caminho + [i[1]])) # adiciona em aberto com f = novo g + distancia heuristica
            custoG[i[1]] = custo # salva custo g

print(caminho)
print(f)