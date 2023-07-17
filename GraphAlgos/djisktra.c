#include<stdio.h>
#include<stdlib.h>
#define INFINITY 9999

void djisktra(int **graph,int n,int src){
	int **cost = (int **)malloc(n * sizeof(int *)); 
    for (int i=0; i<n; i++) {
    	cost[i] = (int *)malloc(n * sizeof(int));
    }
    int *dist  = (int *)malloc(n*sizeof(int));
    int *pred = (int *)malloc(n*sizeof(int));
    int *flag = (int *)malloc(n*sizeof(int));
    int count = 0;
    //pred stores the predecessor of each node
	//count gives the number of nodes seen so far
	
	//cost matrix creation
	for(int i = 0;i<n;i++){
		for (int j = 0;j<n;j++){
			if (graph[i][j] == 0){
				cost[i][j] = INFINITY;
			}
			else {
				cost[i][j] = graph[i][j];
			}
		}
	}

	//initialize pred,dist and flag
	for(int i=0;i<n;i++){
		dist[i]=cost[src][i];
		pred[i]=src;
		flag[i]=0;
	}
	
	dist[src]=0;
	flag[src]=1;
	count=1;
	//while loop stops when all elements are included in Set s
	while(count<n-1){
		int mindist = INFINITY;
		int nextnode;
		//nextnode gives the node at minimum distance i.e. finding which node to take and keep it in set S
		for(int i=0;i<n;i++){
			if(dist[i]<mindist && flag[i] == 0)
			{
				mindist=dist[i];
				nextnode=i;
			}
		}
		//check if a better path exists through nextnode. i.e. relaxation operation			
		flag[nextnode]=1;
		for(int i=0;i<n;i++){
			if(flag[i] ==0){
				if(mindist+cost[nextnode][i]<dist[i])
				{
					dist[i]=mindist+cost[nextnode][i];
					pred[i]=nextnode;
				}
			}
		}
		count++;
	}

	//printing the path and distance of each node
	for(int i=0;i<n;i++){
		if(i != src)
		{
			printf("\nDistance of node%d=%d",i,dist[i]);
			
			printf("\nPath=%d",i);
			int j=i;
			do
			{
				j=pred[j];
				printf("<-%d",j);
			}while(j != src);
			
		}
	}
	printf("\n");
}

 int main(int argc, char const *argv[])
{
	int n;int src; 
    //printf("Enter no. of vertices:");
	scanf("%d",&n);
	//printf("\nEnter the adjacency matrix:\n");
	int **graph = (int **)malloc(n * sizeof(int *)); 
    for (int i=0; i<n; i++) {
    	graph[i] = (int *)malloc(n * sizeof(int));
    }
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			scanf("%d",&graph[i][j]);
		}
	}
	//printf("\nEnter the starting node:");
	scanf("%d",&src);
	djisktra(graph,n,src);
	
	return 0;
}