#include<stdio.h>
#define LIM 5000

typedef struct edge {
    int v, w;
} edge;

edge graph[LIM][LIM];
int vertices;

void addEdge(int v1, int v2, int w) {
    int p = ++graph[v1][0].w;
    graph[v1][p].v = v2;
    graph[v1][p].w = w;
}

void init() {
    int i;
    for(i = 0; i < vertices; i++) {
        graph[i][0].w = 0;
    }
}

void print() {
    int i, j;
    for(i = 0; i < vertices; i++) {
        printf("%d: \t", i);
        for(j = 0; j < graph[i][0].w; j++) {
            printf("%d (%d)\t", graph[i][j].v, graph[i][j].w);
        }
        printf("\n");
    }
}

int main() {
    int v1, v2, w, e;
    scanf("%d %d", &vertices, &e);
    init();
    while(e--) {
        scanf("%d %d %d", &v1, &v2, &w);
        addEdge(v1, v2, w);
    }
    print();
}
