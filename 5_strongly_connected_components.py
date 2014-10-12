#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from heapq import *

'''
    Componentes Fortemente Conexos 
    (http://en.wikipedia.org/wiki/Strongly_connected_components)
    
    Um grafo orientado e fortemente conexo se ha um caminho entre todos os
    vertices dele.
    
    Propriedades e utilidades:
        - Um grafo orientado e aciclico apenas se nao possuir componentes 
        fortemente conexos com mais de um vertice
        - O problema de 2-satisfiability de formulas logicas pode ser 
        resolvido com componentes fortemente conexos
        (http://en.wikipedia.org/wiki/2-satisfiability)
        - Pode-se verificar se um grafo nao direcionado pode ter suas arestas
        orientadas de uma forma a se tornar um grafo fortemente conexo
        (http://en.wikipedia.org/wiki/Robbins_theorem)
'''

graph1 = {
    "a": ["b", "e"],
    "b": ["c"],
    "c": ["d", "f"],
    "d": ["f"],
    "e": ["f"],
    "f": ["a"]
}

graph2 = {
    "a": ["b"],
    "b": ["c", "e", "f"],
    "c": ["d", "g"],
    "d": ["c", "h"],
    "e": ["a", "f"],
    "f": ["g"],
    "g": ["f"],
    "h": ["d", "g"]
}

# funcao utilitaria para imprimir um grafo com formatacao
def printgraph(g):
    for vertex in g.keys():
        print vertex, ":\t",
        for v in g[vertex]:
            print v, "\t",
        print ""

'''
    Algoritmo de Tarjan para Componentes Fortemente Conexos
    (http://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm)
    
    O algoritmo realiza uma busca em profundidade, rotulando os vertices que encontra,
    e colocando-os numa pilha, e determina o vertice de menor indice que pode ser 
    alcancado pelos vertices que encontra. Ao terminar a exploracao em profundidade,
    todos os vertices empilhados, entre o menor vertice alcancavel e o topo da pilha
    pertencem a mesma componente fortemente conexa.
'''

def tarjan(graph):
    global cur_index
    global cur_component
    global indices
    global lowlink
    global components
    global stack
    cur_index = 0
    cur_component = 0
    indices = {}
    lowlink = {}
    components = {}
    stack = []

    # explora o grafo em profundidade a partir de todos os
    # vertices nao explorados (necessario pois quando o 
    # grafo nao e conexo mais de uma busca precisa ser realizada
    for vertex in graph.keys():
        if vertex not in indices:
            strongconnect(vertex, graph)

            
def strongconnect(vertex, graph):
    global cur_index
    global cur_component
    global indices
    global lowlink
    global components
    global stack
    
    # Atribui indice ao vertice atual, e determina seu 
    # ancestral mais distante como ele mesmo
    cur_index += 1
    indices[vertex] = cur_index
    lowlink[vertex] = cur_index
    
    stack.append(vertex)
    
    # para cada vertice ao qual o vertice atual esta conectado
    for w in graph[vertex]:
        if w not in indices:
            # se o vertice nao possui indice, ainda nao foi explorado
            # explora-o e determina o ancestral do vertice atual como
            # sendo o mais distante entre o ja encontrado e o encontrado
            # na exploracao do vertice
            strongconnect(w, graph)
            lowlink[vertex] = min(lowlink[vertex], lowlink[w])
        elif w in stack:
            # se o vertice ja esta na pilha, verifica se ele e o ancestral
            # mais distante do vertice atual
            lowlink[vertex] = min(lowlink[vertex], indices[w])
        
    # quando conclui a exploracao, remove da pilha todos os vertices ate
    # a raiz da componente (primeiro vertice da componente a ser explorado)
    # e rotula todos estes vertices como pertencendo a mesma componente
    if indices[vertex] == lowlink[vertex]:
        cur_component += 1
        while True:
            v = stack.pop()
            components[v] = cur_component
            if v == vertex:
                break

                
tarjan(graph1)
printgraph(graph1)
print "Components: ", components

print ""

tarjan(graph2)
printgraph(graph2)
print "Components: ", components

'''
    Exercicios do SPOJ:
        - Buracos de Minhoca (verificar se o grafo e fortemente conexo)
            (http://br.spoj.pl/problems/BURACOS/)
            
        - Ir e vir (verificar se o grafo e fortemente conexo)
            (http://br.spoj.pl/problems/IREVIR/)
            
        - Serie de tubos (verificar se existe uma orientacao das arestas no
        grafo nao orientado que o tornaria um grafo fortemente conexo)
            (http://br.spoj.pl/problems/TUBOS/)
            
        - Cardapio da Sra. Montagny (2-satisfiability de uma formula)
            (http://br.spoj.pl/problems/CARDAPIO/)
'''
