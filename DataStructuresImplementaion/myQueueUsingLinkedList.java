class myQueueUsingLinkedList<E>{

    private SinglyLinkedList<E> L;
    //Other variables to be defined by student
    
    public myQueueUsingLinkedList(){
        L = new SinglyLinkedList<E>();
        //Other initializations to be done by student
    }
    
    //This method should return the size of the stack
    public int getSize(){
    	return (L.size());
        //To be written by student
    }
    
    //This should implement the enqueue operation of stack
    public void enqueue(E value){
        //To be written by student
              L.addLast(value);
    }
    
    //This should implement the dequeue operation of stack.
    //This method should throw an exception in case the queue is empty.
    public E dequeue() throws Exception{
        //To be written by student
    	if (L.isEmpty()){
    		System.out.println("Queue is Empty");
           throw new Exception();
    		
    	}
    	else {
    	return L.removeFirst();
    	}
    }
}