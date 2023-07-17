#include <stdio.h> 
#include <stdlib.h> 
#include <limits.h> 
  
// A structure to represent a stack 
struct Stack 
{ 
    int top; 
    unsigned capacity; 
    int* array; 
}; 
  
// function to create a stack of given capacity. It initializes size of 
// stack as 0 
struct Stack* createStack(unsigned capacity) 
{ 
    struct Stack* stack = (struct Stack*) malloc(sizeof(struct Stack)); 
    stack->capacity = capacity; 
    stack->top = -1; 
    stack->array = (int*) malloc(stack->capacity * sizeof(int)); 
    return stack; 
} 
  
// Stack is full when top is equal to the last index 
int isFull(struct Stack* stack) 
{   return stack->top == stack->capacity - 1; } 
  
// Stack is empty when top is equal to -1 
int isEmpty(struct Stack* stack) 
{   return stack->top == -1;  } 
  
// Function to add an item to stack.  It increases top by 1 
void push(struct Stack* stack, int item) 
{ 
    if (isFull(stack)) 
        return; 
    stack->array[++stack->top] = item; 
    //printf("%d pushed to stack\n", item); 
} 
  
// Function to remove an item from stack.  It decreases top by 1 
int pop(struct Stack* stack) 
{ 
    if (isEmpty(stack)) 
        return INT_MIN; 
    return stack->array[stack->top--]; 
} 

struct node
{
    int nodenumber;
    struct node* next;
};

struct Graph
{
    int numnodes;
    int* visited;
    struct node** adjLists;//array of linked lists, each element of linked list is a node
};

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
 
    int i;
    for (i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL;
        graph->visited[i] = 0;
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

void topso (struct Graph* graph, int nodenumber,struct Stack* stack){
    graph->visited[nodenumber] = 1;

    struct node* list = graph->adjLists[nodenumber];
        //finding adjacency list of given nodenumber
    struct node* temp = list;
    while(temp != NULL){
        int connectednodenumber = temp->nodenumber;
            //finding out the next connected vertex to the given vertex
        if(graph->visited[connectednodenumber] == 0) {
                //checking if vertex is visited initially or not. if not  do the dfs on it.
            topso(graph, connectednodenumber,stack);

        }
        temp = temp->next;
    }

    push(stack, nodenumber); 
}

void topsort(struct Graph* graph){
    struct Stack* stack = createStack(graph->numnodes + 100);
    for(int i = 0;i<graph->numnodes;i++){
        if(graph->visited[i] == 0){
            topso(graph,i,stack);
        }
    }

    while(isEmpty(stack) != 1){
        printf("%d ", pop(stack));
    }
    printf("\n");
}

int main(int argc, char const *argv[])
{
    struct Graph* graph1 = initiategraph(6);
    addEdge(graph1, 0, 2);
    addEdge(graph1, 2, 4);
    addEdge(graph1, 2, 5);
    addEdge(graph1, 1, 0);
    addEdge(graph1, 1, 3);
    addEdge(graph1, 3, 2);

    
    struct Graph* graph2 = initiategraph(8);
    addEdge(graph2, 0, 3);
    addEdge(graph2, 1, 3);
    addEdge(graph2, 1, 4);
    addEdge(graph2, 2, 4);
    addEdge(graph2, 2, 7);
    addEdge(graph2, 3, 5);
    addEdge(graph2, 3, 6);
    addEdge(graph2, 3, 7);
    addEdge(graph2, 4, 6);

    
    //display(graph);

    topsort(graph1);
    printf("\n");
    topsort(graph2);

    return 0;
}