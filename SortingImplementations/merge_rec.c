#include <stdio.h>
#include <stdlib.h>

void merge(int *a, int l, int m, int r){
    int n1 = m-l+1;
    int n2 = r-m;
    int *temp1 = (int *)malloc(n1*sizeof(int));
    int *temp2 = (int *)malloc(n2*sizeof(int));
    
    for (int i = 0; i < n1; i++) {
        temp1[i] = a[l + i]; 
    }    
    for (int i = 0; i < n2; i++){ 
        temp2[i] = a[m + 1+ i];
    }
    
    int x = 0; // start of temp1 
    int y = 0; // start of temp2 
    int z = l; // start of merged
    while (x < n1 && y < n2) 
    { 
        if (temp1[x] <= temp2[y]) 
        { 
            a[z] = temp1[x]; 
            x++; 
        } 
        else
        { 
            a[z] = temp2[y]; 
            y++; 
        } 
        z++; 
    } 
    
    while (x < n1) 
    { 
        a[z] = temp1[x]; 
        x++; 
        z++; 
    } 
  
    while (y < n2) 
    { 
        a[z] = temp2[y]; 
        y++; 
        z++; 
    } 
    
}
void mergeSort(int *a, int l, int r) 
{ 
    if (l < r) 
    { 
        int m = l+(r-l)/2; 
  
        mergeSort(a, l, m); 
        mergeSort(a, m+1, r); 
  
        merge(a, l, m, r); 
    } 
} 

void print(int *a, int size) 
{ 
    int i; 
    for (i=0; i < size; i++) {
        printf("%d ", a[i]);
    }
    printf("\n"); 
}
int main()
{
    printf("Hello, World!\n");
    int *a = (int *)malloc(5 *sizeof(int));
    a[0] = 6;
    a[1] = 5;
    a[2] = 4;
    a[3] = 3;
    a[4] = 2;
    mergeSort(a, 0,4); 
    print(a,5);
    

    return 0;
}