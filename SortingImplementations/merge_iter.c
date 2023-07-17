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

void mergesort(int *a, int n) 
//This merges in bottomup fashion. in first loop of csiz = 1; it merger two elements of array two form sorted array of two elements,
//Then in next loop it starts taking sorted arrays of size two to merge it to array of size four and keeps on going
{ 
   
   for (int csiz=1; csiz<=n-1; csiz = 2*csiz) 
   { 
       for (int sl=0; sl<n-1; sl += 2*csiz) 
       { 
           int mid = sl + csiz - 1;
           int x;
           if(sl + 2*csiz - 1 >=n-1){
               x = n-1;
           }
           else{
               x = sl + 2*csiz - 1;
           }
           int rt = x;
           merge(a, sl, mid, rt); 
       } 
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
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    print(&arr, n); 
  
    mergesort(&arr, n); 
  
    printf("\nSorted array is \n"); 
    print(&arr, n); 
    return 0; 
} 
