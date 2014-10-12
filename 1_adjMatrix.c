#include<stdio.h>
#define LIM 5000

int graph[LIM][LIM];
int vertices;

void addEdge(int v1, int v2, int w) {
    graph[v1][v2] = w;
}

void init() {
    int i, j;
    for(i = 0; i < vertices; i++) {
        for(j = 0; j < vertices; j++) {
            graph[i][j] = 0;
        }
    }
}

void print() {
    int i, j;
    for(i = 0; i < vertices; i++) {
        printf("%d: \t", i);
        for(j = 0; j < vertices; j++) {
            if(graph[i][j]) {
                printf("%d (%d)\t", j, graph[i][j]);
            }
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
