graph = {
    '1': ['2', '3', '4'],
    '2': ['1', '3', '5'],
    '3': ['1', '2'],
    '4': ['1'],
    '5': ['2']
}

def bfs(G, s):
    visited = [] # lista de vértices visitados (nós pretos) # set todos os brancos
    queue = [] # inicializa a fila

    visited.append(s) # seta com cinza
    queue.append(s)

    while queue:
        u = queue.pop(0)
        print(u, end = ' ') # seta como preto 
        for v in G[u]:
            if v not in visited: # verifica se é branco 
                visited.append(v) 
                queue.append(v)
# main
bfs(graph, '5')