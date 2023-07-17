
import java.io.*;
import java.lang.Integer;

class Entry{
    public int key;//This denotes the key of the entry stored at the node
    public String value;//This denotes the value of the entry stored at the node
    
    public Entry(int k, String v){
        key = k;
        value = v;
    }
}

public class MinHeapArray{
    
    final int MAX_HEAP_SIZE = 1000;//This indicates the maximum size the heap can grow into.
    public Entry[] A;//This is the array of references to entries
    public int size;//This is the number of current entries in the heap
    
    //This is the initialization method for the array based min-heap implementation.
    public MinHeapArray(){
        size = 0;
        A = new Entry[MAX_HEAP_SIZE+1];
    }
    
    
    //This is the initialization method that takes as input an array of entries
    //and performs the bottom up heap construction
    public MinHeapArray(Entry B[], int n){
        
        size = n;
        A = B;
        bottomUpHeapConstruction();
    }
    
    
    //This method implements the bottom-up heap construction.
    public void bottomUpHeapConstruction(){
        //To be written as part of Homework.
    }
    
    //This method swaps the key-value pairs stored at given indices in the array A
    public void swapVals(int p, int q){
        String temp1 = A[p].value;
        int temp2 = A[p].key;
        A[p].key = A[q].key;
        A[p].value = A[q].value;
        A[q].key = temp2;
        A[q].value = temp1;
    }
    
    
    //This is the min() method that returns the minimum element in the heap
    public String min(){
        return(A[1].value);
    }
    
    
    
    //This method returns whether the heap is empty or not
    public boolean isEmpty(){
        if(size == 0)return(true);
        else return(false);
    }
    
    
    //This method implements the up-heap bubble
    /*
    public void upHeapBubble(int i){
        //To be written as part of homework
    }
    */
    
    //This method implements the down heap bubble
    /*
    public void downHeapBubble(int i){
        //To be written as part of homework
    }
    */
    
    //This method is used to insert a new entry into the min heap
    public void insert(int k, String v){
        Entry E = new Entry(k, v);
        A[++size] = E;
        //upHeapBubble(size);
    }
    
    
    
    //This method implements the removeMin() operation
    public String removeMin(){
        
        String result = A[1].value;
        
        //Copy the entry at index "size" to the root
        A[1].key = A[size].key; A[1].value = A[size].value;
        size--;
        //downHeapBubble(root);
        
        return(result);
    }
    
    
    
    //This method just prints the array storing the heap
    //This may be used for debugging
    public void printArray(){
        for(int i=1;i<=size;++i){
            System.out.print("(" + A[i].key + ", " + A[i].value + "), ");
        }
        System.out.println("");
    }
}