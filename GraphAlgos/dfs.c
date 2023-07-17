#include <stdio.h>
#include <stdlib.h>
 
struct node
{
    int nodenumber;
    struct node* next;
};

struct Graph
{
    int numnodes;
    int* visited;
    int *flag;
    struct node** adjLists;//array of linked lists, each element of linked list is a node
};

int cyclehelp (struct Graph* graph, int nodenumber){
    if(graph->visited[nodenumber] == 0){
            graph->visited[nodenumber] = 1;
            graph->flag[nodenumber] = 1;
            struct node* list = graph->adjLists[nodenumber];
            //finding adjacency list of given nodenumber
            struct node* temp = list;
            while(temp != NULL){
                int connectednodenumber = temp->nodenumber;
                if(graph->visited[connectednodenumber] ==0 && cyclehelp(graph,connectednodenumber)){
                    //printf("back edge detected %d -> %d\n",nodenumber,connectednodenumber);
                    return 1;
                }
                else if (graph->flag[connectednodenumber] == 1){
                    printf("back edge detected %d -> %d\n",nodenumber,connectednodenumber);
                    return 1;
                }
                temp = temp->next;
            }
    }
    graph->flag[nodenumber] = 0;
    return 0;
}

int cycle (struct Graph* graph){
    for (int i = 0;i<graph->numnodes;i++){
        if(cyclehelp(graph,i)){
            printf("cycle present\n");
            return 1;
        }
    }
    return 0;
}
void DFS(struct Graph* graph, int nodenumber,int parent,int count){
        struct node* list = graph->adjLists[nodenumber];
        //finding adjacency list of given nodenumber
        struct node* temp = list;
        
        graph->visited[nodenumber] = 1;
        count++;
        //making current vertex visited to  be 1
        printf("Visited %d", nodenumber);
        printf("||edge is %d,%d",parent ,nodenumber);
        printf("\n");
        while(temp!=NULL) {
            int connectednodenumber = temp->nodenumber;
            //finding out the next connected vertex to the given vertex
            if(graph->visited[connectednodenumber] == 0) {
                //checking if vertex is visited initially or not. if not  do the dfs on it.
                DFS(graph, connectednodenumber,nodenumber,count);
            }
            //if vertex was visited, go on to next vertex in linked list.
            temp = temp->next;
        }
        //new dfs that is not rechable

        if(count <graph->numnodes){
            for(int i = 0;i<graph->numnodes;i++){
                if(graph->visited[i] == 0){
                    DFS(graph,i,i,count);
                }
            }
        }       
}

 
struct node* initiatenode(int v)
{
    struct node* newNode = malloc(sizeof(struct node));
    newNode->nodenumber = v;
    newNode->next = NULL;
    return newNode;
}

struct Graph* initiategraph(int vertices)
{
    struct Graph* graph = malloc(sizeof(struct Graph));
    graph->numnodes = vertices;
 
    graph->adjLists = malloc(vertices * sizeof(struct node*));
    
    graph->visited = malloc(vertices * sizeof(int));
    graph->flag = malloc(vertices * sizeof(int));
 
    int i;
    for (i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL;
        graph->visited[i] = 0;
        graph->flag[i] = 0;
    }
    return graph;
}
 
void addEdge(struct Graph* graph, int source, int dest)
{
    struct node* temp = initiatenode(dest);
    //making a newnode for destination
    temp->next = graph->adjLists[source];
    //making the current nodes next to be the entire list of source
    graph->adjLists[source] = temp;
    //adding newnode on head of linked list for source
 }
 
void display(struct Graph* graph)
{
    for (int i = 0; i < graph->numnodes; i++)
    {
        struct node* temp = graph->adjLists[i];
        printf("\n Adjacency list of node %d\n ", i);
        while (temp)
        {
            printf("%d -> ", temp->nodenumber);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main()
{
    //printf("DFS of graph 1 below................................................\n");
    struct Graph* graph1 = initiategraph(8);
    addEdge(graph1,0,1);
    addEdge(graph1,1,0);

    addEdge(graph1,0,2);
    addEdge(graph1,2,0);

    addEdge(graph1,0,4);
    addEdge(graph1,4,0);

    addEdge(graph1,1,2);
    addEdge(graph1,2,1);

    addEdge(graph1,1,5);
    addEdge(graph1,5,1);

    addEdge(graph1,5,3);
    addEdge(graph1,3,5);

    addEdge(graph1,2,3);
    addEdge(graph1,3,2);

    addEdge(graph1,3,4);
    addEdge(graph1,4,3);

    addEdge(graph1,3,6);
    addEdge(graph1,6,3);

    addEdge(graph1,5,7);
    addEdge(graph1,7,5);

    addEdge(graph1,6,7);
    addEdge(graph1,7,6);
   // DFS(graph1, 3,3,0);
   // printf("DFS of graph2 below................................................\n");
    /////////////////////////////////

    struct Graph* graph2 = initiategraph(6);
    addEdge(graph2,0,1);
    addEdge(graph2,2,1);
    addEdge(graph2,2,3);
    addEdge(graph2,3,4);
    addEdge(graph2,5,4);
    addEdge(graph2,1,4);
    addEdge(graph2,0,5);
    addEdge(graph2,1,5);
    addEdge(graph2,4,0);
   // DFS(graph2,0,0,0);
    //printf("DFS of graph 3 below................................................\n");
    /////////////////////////////////
    struct Graph* graph3 = initiategraph(10);
    addEdge(graph3,3,2);
    addEdge(graph3,2,3);

    addEdge(graph3,3,4);
    addEdge(graph3,4,3);

    addEdge(graph3,4,2);
    addEdge(graph3,2,4);

    addEdge(graph3,1,2);
    addEdge(graph3,2,1);

    addEdge(graph3,1,0);
    addEdge(graph3,0,1);

    addEdge(graph3,1,5);
    addEdge(graph3,5,1);

    addEdge(graph3,5,6);
    addEdge(graph3,6,5);

    addEdge(graph3,0,6);
    addEdge(graph3,6,0);

    addEdge(graph3,6,7);
    addEdge(graph3,7,6);

    addEdge(graph3,7,8);
    addEdge(graph3,8,7);

    addEdge(graph3,8,9);
    addEdge(graph3,9,8);
    
    addEdge(graph3,7,9);
    addEdge(graph3,9,7);
   // DFS(graph3,0,0,0);
   // printf("DFS of graph 4  below................................................\n");
    ////////////////////////////
    struct Graph* graph4 = initiategraph(14);
    addEdge(graph4,0,1);
    addEdge(graph4,1,0);

    addEdge(graph4,0,2);
    addEdge(graph4,2,0);

    addEdge(graph4,3,2);
    addEdge(graph4,2,3);
    
    addEdge(graph4,3,1);
    addEdge(graph4,1,3);

    addEdge(graph4,3,4);
    addEdge(graph4,4,3);

    addEdge(graph4,4,5);
    addEdge(graph4,5,4);

    addEdge(graph4,6,5);
    addEdge(graph4,5,6);

    addEdge(graph4,6,7);
    addEdge(graph4,7,6);

    addEdge(graph4,6,11);
    addEdge(graph4,11,6);

    addEdge(graph4,11,13);
    addEdge(graph4,13,11);

    addEdge(graph4,11,12);
    addEdge(graph4,12,11);

    addEdge(graph4,10,12);
    addEdge(graph4,12,10);

    addEdge(graph4,6,8);
    addEdge(graph4,8,6);

    addEdge(graph4,8,9);
    addEdge(graph4,9,8);

    addEdge(graph4,9,10);
    addEdge(graph4,10,9);

    addEdge(graph4,8,10);
    addEdge(graph4,10,8);
    //DFS(graph4,0,0,0);
    //printf("DFS of graph 5 below................................................\n");
    //////////////////////////////////
    struct Graph* graph5 = initiategraph(8);

    addEdge(graph5,0,1);
    addEdge(graph5,0,2);
    addEdge(graph5,0,4);
    addEdge(graph5,5,1);
    addEdge(graph5,0,5);
    addEdge(graph5,3,0);
    addEdge(graph5,2,3);
    addEdge(graph5,3,7);
    addEdge(graph5,7,6);
    addEdge(graph5,4,6);
    addEdge(graph5,4,5);
    addEdge(graph5,4,7);
    addEdge(graph5,5,6);
    //DFS(graph5,6,6,0);
    cycle (graph1);
    cycle(graph5);

    return 0;
}