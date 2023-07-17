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
    int p = a[h];   
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
  

void quicksort (int *a, int l, int h) 
{ 
    int ma[ h - l + 1 ]; 
  
    int t = -1; 
  
    ma[ ++t ] = l; 
    ma[ ++t ] = h; 
  
    while ( t >= 0 ) 
    { 
        h = ma[ t-- ]; 
        l = ma[ t-- ]; 
  
        int p = divide( a, l, h ); 
  
        if ( p-1 > l ) 
        { 
            ma[ ++t ] = l; 
            ma[ ++t ] = p - 1; 
        } 
  
        if ( p+1 < h ) 
        { 
            ma[ ++t ] = p + 1; 
            ma[ ++t ] = h; 
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
    int arr[] = {10, 7, 8, 9, 1, 5}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    quicksort(&arr, 0, n-1); 
    print(&arr, n); 
    return 0; 
} 