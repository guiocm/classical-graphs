#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# funcao utilitaria para imprimir um grafo, representado
# como matriz, com formatacao
def printgraph(g):
    for indV in range(len(g)):
        print indV, ":\t",
        for indW in range(len(g)):
            if g[indV][indW]:
                print "%d (%d)\t" % (indW, g[indV][indW]),
        print ""
    print ""

# infinito...
infinity = 10**100
        
# matriz de capacidades das arestas do grafo
capacity_matrix = [
    [0,3,0,3,0,0,0],
    [0,0,4,0,0,0,0],
    [3,0,0,1,2,0,0],
    [0,0,0,0,2,6,0],
    [0,1,0,0,0,0,1],
    [0,0,0,0,0,0,9],
    [0,0,0,0,0,0,0]
]

# lista dos vizinhos de cada vertice
# vizinhos de v:
#    todos os vertices u tais que
#    u -> v ou v -> u
neighbors = [
    [1,2,3],
    [0,2,4],
    [0,1,3,4],
    [0,2,4,5],
    [1,2,3,6],
    [3,6],
    [4,5]
]

# grafo inicial, como representado pelas capacidades das arestas
printgraph(capacity_matrix)

'''
    Algoritmo de Edmonds-Karp para fluxo maximo.
    Baseia-se no metodo de Ford-fulkerson, que consiste em
    encontrar "caminhos aumentantes" da fonte ao sorvedouro.
    Os caminhos sao ditos aumentantes pois a cada passo e 
    utilizado um caminho com o menor numero de arestas,
    fazendo com que o numero de arestas dos caminhos encontrados
    sempre aumente.
    
    O algoritmo mantem uma matriz de fluxos, onde a cada fluxo passado
    acrescenta seu valor positivo as arestas no sentido fonte -> sorvedouro,
    assim como seu valor negativo no sentido sorvedouro -> fonte.
    Com esta tecnica, a computacao da capacidade atual de uma aresta permite
    reverter fluxos passados, de maneira a obter o fluxo maximo total.
'''
def edmonds_karp(capacity_matrix, neighbors, source, sink):
    maxflow = 0
    n_vertices = len(capacity_matrix)
    flow_matrix = [[0 for col in range(n_vertices)] for row in range(n_vertices)]
    
    while True:
        # busca um caminho com uma busca em largura
        flow, path = breadth_first_search(  capacity_matrix, 
                                            neighbors, 
                                            source, 
                                            sink, 
                                            flow_matrix)
        
        print flow, path
        
        # se o caminho encontrado tem fluxo igual a zero,
        # nao ha mais caminhos restantes
        if flow == 0:
            break
        
        maxflow += flow
        
        # percorre o caminho encontrado, atualizando a matriz de fluxos
        current = sink
        while current != source:
            next = path[current]
            flow_matrix[current][next] -= flow
            flow_matrix[next][current] += flow
            current = next
    
    return (maxflow, flow_matrix)
    
'''
    Busca em largura para encontrar caminhos aumentantes para o fluxo.
'''
def breadth_first_search(capacity_matrix, neighbors, source, sink, flow_matrix):
    # path aponta os vertices-pai de cada vertice, na busca
    path = [-1 for vertex in range(len(neighbors))]
    path[source] = -2
    
    # capacities armazena a capacidade do fluxo da fonte ate cada 
    # vertice encontrado no caminho
    capacities = [0 for vertex in range(len(neighbors))]
    capacities[source] = infinity
    
    queue = []
    queue.append(source)
    
    while queue:
        current = queue.pop(0)
        for vertex in neighbors[current]:
            # capacidade atual da aresta
            # como na matriz de fluxos sao adicionadas capacidades negativas
            # no sentido contrario ao do fluxo, uma aresta que esta sendo
            # percorrida no sentido contrario tera capacidade positiva
            edge_capacity = capacity_matrix[current][vertex] - flow_matrix[current][vertex]
            
            # explora o vertice, se sua aresta ainda tem capacidade para fluxo, 
            # e o vertice ainda nao foi explorado nesta busca
            if edge_capacity > 0 and path[vertex] == -1:
                path[vertex] = current
                capacities[vertex] = min(capacities[current], edge_capacity)
                
                if vertex != sink:
                    queue.append(vertex)
                else:
                    # a busca retorna ao encontrar o primeiro caminho ate o sorvedouro
                    return capacities[sink], path
    
    # ou quando nenhum caminho e encontrado (flow = 0, que indica o fim do algoritmo)
    return 0, path

print ""
flow, path = edmonds_karp(capacity_matrix, neighbors, 0, 6)
print flow
printgraph(path)

'''
    links de referencia:
        Redes de fluxo
            http://en.wikipedia.org/wiki/Flow_network
        Teorema de fluxo maximo - corte minimo
            http://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
        Algoritmo de Ford-Fulkerson 
            http://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
        Algoritmo de Edmonds-Karp
            http://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
        
        Problema do SPOJ usando fluxo (A Lei Vai a Cavalo)
            http://br.spoj.pl/problems/CAVALOS
'''
