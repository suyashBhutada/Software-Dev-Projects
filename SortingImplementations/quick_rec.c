#include<stdio.h> 
#include<stdlib.h>

void exchange(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 

int divide (int *a, int l, int h) 
{ 
    int p = a[h]; //pivot is last element  
    int i = (l - 1);
  
    for (int j = l; j < h; j++) 
    { 
        if (a[j] <= p) 
        { 
            i++; 
            exchange(a+ i, a+j); 
        } 
    } 
    exchange(a+i + 1, a+h); 
    return (i + 1); 
} 
  
void quickSort(int *a, int l, int h) 
{ 
    if (l < h) 
    { 
        int p = divide(a, l, h); //dividing the array according to pivot
  
        quickSort(a, l, p - 1); 
        quickSort(a, p + 1, h); 
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
    int arr[] = {10, 7, 8, 9, 1, 5}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    quickSort(&arr, 0, n-1); 
    printf("Sorted array: n"); 
    print(&arr, n); 
    return 0; 
} 