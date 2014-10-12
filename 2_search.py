#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
    Representacao de um grafo atraves de lista de adjacencias
    (usando dicionarios de Python -- hashtables)
    
    graph[v] 
        recupera a lista de vertices ligados a v
    graph[v].append(w) 
        adiciona w a lista de vertices ligados a v
    w in graph[v]
        verifica se ha uma aresta v --> w
    
'''

graph = {
    1: [2, 3, 6],
    2: [1, 3, 4],
    3: [1, 2, 5],
    4: [2, 5],
    5: [3, 4, 8],
    6: [1, 7],
    7: [6, 8],
    8: [5, 7]
}

'''
    buscas em largura e profundidade
    
    aplicacoes:
        conectividade
        biparticao
        ordenacao topologica
        ponto de partida de algoritmos mais complexos
            Tarjan (arestas de corte) usa busca em profundidade
            Ford-Fulkerson (fluxo maximo) usa busca em largura
            Dijkstra e A* (melhor caminho) e Prim (AGM) usam uma busca com fila de prioridades

'''

# busca em largura

def bfs(g, v):
    status = {}
    for vertex in g.keys():
        status[vertex] = "undiscovered"
    
    queue = []
    
    queue.append(v)
    status[v] = "discovered"
    print "vertex ", v, " ", status[v]
    
    while queue:
        current = queue.pop(0)
        print "exploring vertex ", current
        
        for w in g[current]:
            if status[w] == "undiscovered":
                queue.append(w)
                status[w] = "discovered"
                print "vertex ", w, " ", status[w]
            
        status[current] = "explored"
        print "vertex ", current, " ", status[current]
 
        
bfs(graph, 1)
print ""


# busca em profundidade

def depthfirst(g, v):
    
    def dfs(v):
        print "exploring vertex ", v
        for w in g[v]:
            if status[w] == "undiscovered":
                status[w] = "discovered"
                print "vertex ", w, " ", status[w]
                dfs(w)
        status[v] = "explored"
        print "vertex ", v, " ", status[v]
        
    status = {}
    for vertex in g.keys():
        status[vertex] = "undiscovered"
    
    status[v] = "discovered"
    print "vertex ", v, " ", status[v]
    dfs(v)
    
depthfirst(graph, 1)
print ""


# busca em profundidade sem closure...

def depthFirstSearch(g, v):
    status = {}
    for vertex in g.keys():
        status[vertex] = "undiscovered"
        
    status[v] = "discovered"
    explorer(g, v, status)
  
def explorer(g, v, status):
    print "exploring vertex ", v
    for w in g[v]:
        if status[w] == "undiscovered":
            status[w] = "discovered"
            print "vertex ", w, " ", status[w]
            explorer(g, w, status)
    status[v] = "explored"
    print "vertex ", v, " ", status[v]

depthFirstSearch(graph, 1)


'''
    problemas do br.spoj.pl que podem ser resolvidos com buscas simples:
        
        http://br.spoj.pl/problems/ENERGIA/
            detectar conectividade
            
        http://br.spoj.pl/problems/DENGUE/
            escolher a raiz para uma árvore que minimiza a altura máxima dela
            
        http://br.spoj.pl/problems/MESA/
            detectar se um grafo é bipartido

    alguns links a respeito do minimax (e alpha-beta pruning), que foram comentados em aula:
        http://en.wikipedia.org/wiki/Minimax
        http://en.wikipedia.org/wiki/Alpha-beta_pruning
        http://chessprogramming.wikispaces.com/Minimax

'''
