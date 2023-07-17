#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct{
	size_t element_size; // generic => need to store this
	unsigned int num_allocated, num_used;
	void *array; // Using one-based indexing
	int (*comparator)(void *, int, int); // Returns -ve, 0, or +ve
}HEAP;
void initHeap(HEAP *h, size_t element_size,int (*comparator)(void *, int, int)){ // Continued
	//printf("here it is\n");
	h->element_size = element_size;
	h->num_allocated = 10;
	h->num_used = 0;

	
	if(NULL == (h->array = malloc(h->num_allocated * element_size))){
		printf("Out of memory\n");
		return;
	}
	//printf("here it is 2\n");
	h->comparator = comparator;
	return;
}


static void swap(HEAP *h, int i, int j){
// Using one-based indexing (h->array[0] is used in swapping)
	char *ip = (char *) h->array + i * h->element_size;
	char *jp = (char *) h->array + j * h->element_size;
	char *tp = (char *) h->array;
	memcpy((void *) tp, (void *) ip, h->element_size);
	memcpy((void *) ip, (void *) jp, h->element_size);
	memcpy((void *) jp, (void *) tp, h->element_size);
	return;
}
static int compare_int(void *array, int i1, int i2){
	int n1 = *((int *) array + i1);
	int n2 = *((int *) array + i2);
	return (n1 - n2);
}
static void swapUp(HEAP *h, int k){
	while (k > 1 && (h->comparator(h->array, k/2, k) > 0)){
	swap(h, k, k/2);
	k = k/2;
	}
	return;
}
void insert(HEAP *h, void *x){
// Make sure there is space for another element
	if(h->num_used + 1 == h->num_allocated){
	h->num_allocated *= 2;
	if(NULL == (h->array = realloc(h->array,h->num_allocated * h->element_size))){
		printf("insert: Out of memory");
		return;
		//exit(-1);
		}	
	}
	// Insert element at the end
	h->num_used++;
	memcpy((char *) h->array + h->num_used * h->element_size, x, h->element_size);
	/* Restore heap property */
	swapUp(h, h->num_used);
	return;
}
static void swapDown(HEAP *h, int k){
	while (2*k <= h->num_used) {
	int j = 2*k;
	// Choose child with larger key
	if(j < h->num_used && (h->comparator(h->array, j, j+1) > 0))
	j++;
	if(h->comparator(h->array, k, j) <= 0)
	break;
	swap(h, k, j);
	k = j;
	}
	return;
}
void deleteMin(HEAP *h, void *min){
// Max is at the root (index 1)

	memcpy(min, h->array + h->element_size, h->element_size);
	// Copy last element to root
	memcpy(h->array + h->element_size,
	h->array + h->num_used * h->element_size, h->element_size);
	h->num_used--;
	// Restore heap property
	swapDown(h, 1);
	return;
}

void print(int *a, int size) 
{ 
    int i; 
    for (i=0; i < size; i++) {
        printf("%d ", a[i]);
    }
    printf("\n"); 
}

int main(int argc, char const *argv[])
{
	int n = 10;
	HEAP myheap;
	initHeap(&myheap, sizeof(int), compare_int);
	
	for(int i = 0;i<n;i++){
		int key;
		key = (rand())%100;
		int *k = &key;
		insert(&myheap, k);	
	}
	int sum = 0;
	HEAP *hp = &myheap;
	int *a = (int *)malloc(n*sizeof(int));
	int f = 0;
	while(hp->num_used>0){
		int *temp1 = (int *)malloc(sizeof(int));
		deleteMin(hp,temp1);
		a[f] = *temp1;
		f++;
	}
	print(a,n);
	return 0;
}