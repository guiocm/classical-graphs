#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from heapq import *
import random
 
random.seed()

print "enter start and end nodes for search"
begin = str(raw_input())
end = str(raw_input())

# funcao utilitaria para imprimir um grafo com formatacao
def printgraph(g):
    for vertex in g.keys():
        print vertex, ":\t",
        for v, w in g[vertex]:
            print v, "(", w, ")\t\t",
        print ""

# os rotulos dos vertices foram alterados para strings
graph = {
    "a": [("b", 5), ("e", 3)],
    "b": [("a", 5), ("c", 7), ("f", 2)],
    "c": [("b", 7), ("e", 1), ("f", 1), ("h", 8)],
    "d": [("e", 2), ("g", 4)],
    "e": [("a", 3), ("c", 1), ("d", 2), ("g", 9)],
    "f": [("b", 2), ("c", 1), ("h", 6)],
    "g": [("d", 4), ("e", 9), ("h", 3)],
    "h": [("c", 8), ("f", 6), ("g", 3)]
}

'''
    http://en.wikipedia.org/wiki/Dijkstra's_algorithm
    algoritmo de dijkstra realiza uma "best-first search"
    em que o proximo vertice a ser explorado e o de menor custo
    geral nao explorado no momento.
    
    busca o caminho minimo do vertice begin ao vertice end, 
    retorna a arvore de caminhos minimos a partir de begin
    gerada na exploracao ate encontrar o vertice end
    "verbose" ativa ou desativa a impressao das mensagens
'''
def dijkstra(graph, begin, end, verbose=True):
    bpt = {}
    costs = {}
    
    queue = []
    bpt[begin] = []
    costs[begin] = 0
    
    for vertex, weight in graph[begin]:
        heappush(queue, (weight, (begin, vertex)))
    
    if verbose:
        print "adding vertex", begin
    while queue and end not in bpt:
        best = heappop(queue)
        cost, vertices = best
        v1, v2 = vertices
        
        if v2 not in bpt:
            if verbose:
                print "adding vertex", v2, "connected to", v1, "with cost", cost
            costs[v2] = cost
            
            for vertex, weight in graph[v1]:
                if vertex is v2:
                    break
                    
            bpt[v1].append((v2, weight))
            bpt[v2] = [(v1, weight)]
            for vertex, wgh in graph[v2]:
                if vertex is not v1:
                    heappush(queue, (wgh + cost, (v2, vertex)))
    
    return bpt

print "Dijkstra's Algorithm"
bpt = dijkstra(graph, begin, end)
printgraph(bpt)
print ""

def dijkstra_heuristic(begin, end):
    return 0

def useless_heuristic(begin, end):
    return int(20*random.random())
    
'''
    Uma heuristica e admissivel se ela jamais superestima custos
    http://en.wikipedia.org/wiki/Admissible_heuristic
'''
def admissible_heuristic(begin, end):
    q = [(begin, 0)]
    proc = set()
    while q:
        vertex, height = q.pop()
        if vertex is end:
            return height
        proc.add(vertex)
        for v, w in graph[vertex]:
            if v is not vertex and v not in proc:
                q.append((v, height+1))
    return float("inf")

'''
    http://en.wikipedia.org/wiki/A*_search_algorithm
    algoritmo A* consiste em uma generalizacao do algoritmo de Dijkstra
    em que uma heuristica e utilizada para estimar a distancia restante entre
    algum vertice e o vertice de destino.
    
    
    busca o caminho minimo do vertice begin
    ao vertice end, retorna a arvore de caminhos minimos a partir de begin
    gerada na exploracao ate encontrar o vertice end
    "verbose" ativa ou desativa a impressao das mensagens
'''
def a_star(graph, heuristic, begin, end, verbose=True):
    bpt = {}
    costs = {}
    
    queue = []
    bpt[begin] = []
    costs[begin] = 0
    
    for vertex, weight in graph[begin]:
        heappush(queue, (weight + heuristic(vertex, end), (begin, vertex)))
    
    if verbose:
        print "adding vertex", begin
    while queue and end not in bpt:
        best = heappop(queue)
        h, vertices = best
        v1, v2 = vertices
        
        if v2 not in bpt:
            for vertex, edge_cost in graph[v1]:
                if vertex is v2:
                    break
            cost = costs[v1] + edge_cost
            if verbose:
                print "adding vertex", v2, "connected to", v1, "with cost", cost, "( f =", h, ")"
            costs[v2] = cost
            
            for vertex, weight in graph[v1]:
                if vertex is v2:
                    break
                    
            bpt[v1].append((v2, weight))
            bpt[v2] = [(v1, weight)]
            for vertex, wgh in graph[v2]:
                if vertex is not v1:
                    heappush(queue, (cost + wgh + heuristic(vertex, end), (v2, vertex)))
    
    return bpt

print "A* with non-admissible heuristic"
bpt = a_star(graph, useless_heuristic, begin, end)
printgraph(bpt)
print ""

print "A* with Dijkstra's heuristic ( h = 0 always )"
bpt = a_star(graph, dijkstra_heuristic, begin, end)
printgraph(bpt)
print ""

print "A* with some admissible heuristic ( h = number of edges between two nodes )"
bpt = a_star(graph, admissible_heuristic, begin, end)
printgraph(bpt)
print ""
