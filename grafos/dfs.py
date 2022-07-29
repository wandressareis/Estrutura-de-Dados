# Busca em profundidade/Depth-First 
# 1. Começaremos colocando qualquer um dos vértices do grafo no topo da pilha.
# 2. Depois disso, pegue o item do topo da pilha e adicione-o à lista visitada do vértice.
# 3. Em seguida, crie uma lista desse nó adjacente do vértice. Adicione aqueles que não estão na lista de vértices visitados ao topo da pilha.
# #

graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'], 
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = set() 

def dfs(visited, graph, node): 
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, '5')

# Print: 5 3 2 4 8 7