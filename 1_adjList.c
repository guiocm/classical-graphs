#include<stdio.h>
#include<stdlib.h>
#define LIM 5000
 
typedef struct node {
    struct node *next;
    int vertex;
    int weight;
} edge;
 
edge *graph[LIM];
int vertices;
 
void addEdge(int v1, int v2, int w) {
    edge *e = (edge*)malloc(sizeof(edge));
    e->next = graph[v1];
    e->vertex = v2;
    e->weight = w;
    graph[v1] = e;
}
 
void init() {
    int i;
    for(i = 0; i < vertices; i++)
        graph[i] = NULL;
}
 
void print() {
    int i = 0;
    edge *e;
    while(i < vertices) {
        e = graph[i];
        printf("%d: \t", i++);
        while(e != NULL) {
            printf("%d (%d)\t", e->vertex, e->weight);
            e = e->next;
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
