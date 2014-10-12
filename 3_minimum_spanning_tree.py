#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from heapq import *

'''
    Grafos - Aula 3
    Arvore geradora minima: algoritmos de Prim e Kruskal

    Inicialmente: http://en.wikipedia.org/wiki/Cut_(graph_theory)
    
    Um Corte, em teoria de Grafos, e a divisao dos vertices do grafo
    em dois subconjuntos, onde cada vertice deve estar em um (e apenas um)
    subconjunto (subconjuntos disjuntos).
    As arestas de um corte sao as arestas que ligam vertices de subconjuntos
    diferentes.
'''

'''
    nas implementacoes foi utilizada uma fila de prioridades da biblioteca heapq de python.
    duas funcoes dela foram utilizadas:
    - adicionar um elemento a ela
        heappush(fila, (prioridade, elemento)) 
            adiciona a fila o elemento com uma prioridade 
    - retornar o elemento com o menor prioridade
        heappop(fila)
            retorna o elemento com menor prioridade da fila (e o remove da fila)
'''

# cada aresta agora e representada por um par (vertice, peso) nas listas de adjacencias
graph = {
    1: [(2, 11), (3, 3), (6, 5)],
    2: [(1, 11), (3, 10), (4, 8)],
    3: [(1, 3), (2, 10), (5, 2)],
    4: [(2, 8), (5, 6)],
    5: [(3, 2), (4, 6), (8, 7)],
    6: [(1, 5), (7, 12)],
    7: [(6, 12), (8, 3)],
    8: [(5, 7), (7, 3)]
}

# funcao utilitaria para imprimir um grafo com formatacao
def printgraph(g):
    for vertex in g.keys():
        print vertex, ":\t",
        for v, w in mst[vertex]:
            print v, "(", w, ")\t\t",
        print ""

'''
    http://en.wikipedia.org/wiki/Prim%27s_algorithm
    
    Algoritmo de Prim inicia a arvore de um vertice arbitrario,
    e a expande selecionando a aresta de menor custo do corte, ate
    que a arvore inclua todos os vertices do grafo (corte sem arestas).
    
    O Algoritmo de Prim requer que o grafo seja conectado (apenas uma componente),
    mas pode ser adaptado para grafos nao conectados (rodando o algoritmo em todas as
    componentes individualmente).
'''

def prim(graph):
    mst = {}
    
    queue = []
    begin = graph.keys()[0]
    mst[begin] = []
    
    for vertex, weight in graph[begin]:
        heappush(queue, (weight, (begin, vertex)))
    
    print "adding vertex", begin
    while queue:
        best = heappop(queue)
        weight, vertices = best
        v1, v2 = vertices
        
        if v2 not in mst:
            print "adding vertex", v2, "connected to", v1
            mst[v1].append((v2, weight))
            mst[v2] = [(v1, weight)]
            for vertex, wgh in graph[v2]:
                if vertex is not v1:
                    heappush(queue, (wgh, (v2, vertex)))
    
    return mst
    
mst = prim(graph)
printgraph(mst)
print ""

'''
    http://en.wikipedia.org/wiki/Kruskal's_algorithm
    
    Enquanto o Algoritmo de Prim opera expandindo o grafo a partir de um vertice inicial,
    o Algoritmo de Kruskal sempre processa, a cada passo, a aresta de menor custo do grafo,
    mas so inclui esta aresta na arvore geradora minima se ele conectar grupos de vertices que
    ainda nao estavam conectados. (se a aresta selecionada estiver entre dois vertices que ja
    foram conectados por arestas incluidas anteriormentes, ela e descartada).
    
    O algoritmo precisa de uma lista ordenada (ao menos parcialmente) das arestas 
    (fila de prioridades e suficiente). Alem de uma estrutura de conjuntos disjuntos (usada para 
    controlar quais vertices ja estao no mesmo grupo). A eficiencia dessa estrutura influenciara
    a eficiencia geral do algoritmo.    
    http://en.wikipedia.org/wiki/Disjoint-set_data_structure
'''

def recoverparent(v, par):
    while par[v] != v:
        v = par[v]
    return v

def kruskal(graph):
    mst = {}
    parents = {}
    for vertex in graph.keys():
        mst[vertex] = []
        parents[vertex] = vertex
        
    queue = []
    for vertex in graph.keys():
        for v2, weight in graph[vertex]:
            # esta checagem apenas impede que as arestas sejam adicionadas duas vezes, por ser
            # um grafo nao orientado
            if vertex < v2:
                heappush(queue, (weight, (vertex, v2)))
    
    while queue:
        best = heappop(queue)
        weight, vertices = best
        v1, v2 = vertices
        
        p1 = recoverparent(v1, parents)
        p2 = recoverparent(v2, parents)
        if p1 != p2:
            print "adding edge between", v1, v2
            parents[p2] = p1
            mst[v1].append((v2, weight))
            mst[v2].append((v1, weight))
        else:
            print "skipping edge between", v1, v2
    
    return mst

mst = kruskal(graph)
printgraph(mst)

'''
    exercicio: http://br.spoj.pl/problems/REDOTICA/
'''
