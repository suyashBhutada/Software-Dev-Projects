import java.io.*;
import java.lang.Integer;

class Node{
    public int key;//This denotes the key stored at the node
    public String value;//This denotes the value stored in the node.
    public Node leftChild;//This is a reference to the left child in the binary tree
    public Node rightChild;//This is a reference to the right child in the binary tree
    public Node parent;//This is a reference to the parent of the node in the binary tree.
    
    public Node(){
        parent = leftChild = rightChild = null;
    }
}

public class BinarySearchTree {
	public Node root;
    public int size;
    
    //This is the initialization method for Binary Search Tree.
    public BinarySearchTree(){
        
        size = 0;
        root = null;
    }
    
    //This method checks if the given node is a leaf
    public boolean isLeaf(Node N){
        if(N.leftChild == null && N.rightChild == null)return(true);
        else return(false);
    }
    
    
    //This method implements the get method discussed in class.
    public String get(int k){
        //To be written as part of Homework
    	if (root == null){
    		return null;
    	}
    	if (root.key == k){
    		return root.value;
    	}
    	else if (k>root.key){
    		root = root.rightChild;
    		return get (k);
    	}
    	else {
    		root = root.leftChild;
    		return get(k);
    	}
    }
    
    
    //This method implements the put method discussed in class.
    public String put(int k, String v){
        //To be written as part of Homework
    	if (root == null){
    		root.key = k;
    		root.value = v;
    		root.leftChild = null;
    		root.rightChild = null;
    	}
    	if (k>root.key){
    		root = root.rightChild;
    		put(k,v);
    	}
    	else {
    		root = root.leftChild;
    		put (k,v);
    	}
    	return v;
    }
    
    //This method implements the remove method discussed in class
    public void remove(int k){
        //To be written as part of Homework.
    	if (root==null){
    		return ;
    	}
    	if (k==root.key){
    		if(root.rightChild == null){
    			root = root.leftChild;
    			
    		}
    		else {
    			
    		}
    	}
    }
}

