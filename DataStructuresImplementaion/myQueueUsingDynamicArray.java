class myQueueUsingDynamicArray{

    private dynamicArray A;
    //Other variables to be defined by student
    private int length;
    //maintains length of given array
    
    public myQueueUsingDynamicArray(int length){
        A = new dynamicArray();
        length = 0;
        //Other initializations to be done by student
    }
    
    //This method should return the number of elements in the queue
    public int getSize(){
        //To be written by student
    	return (length);
    }
    
    //This should implement the enqueue operation of Queue
    public void enqueue(int value){
        //To be written by student
    	if (length == A.getSize()){
    		A.doubleSize();
    		try {
				A.modifyElement(value, length);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    		
    		length = length + 1; 
    		
    	}
    	else {
    		try {
				A.modifyElement(value,length);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    		length = length + 1;
    	}
    	}
    
    
    //This should implement the dequeue operation of Queue
    //This method should throw an exception in case the queue is empty.
    public int dequeue() throws Exception {
        //To be written by student
    	if (length==0){
    		System.out.println("Queue is empty. no dequeue is possible");
            throw new Exception();
    		
        }
    	else {
    		int s = 0;
			try {
				s = A.getElement(0);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	for (int i = 1; i<=A.getSize()-1;i++){
    		try {
				A.modifyElement(A.getElement(i), i-1);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	}
    	try {
			A.modifyElement(0, A.getSize()-1);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	length = length -1;
    	if (length>0 && 2*length < A.getSize()){
        	A.halveSize();
        	return s;
        }
        else {
        	return s;
        }
    }
    }
   public void display () throws Exception{
    	for (int i = 0; i<=length-1;i++){
    		System.out.println(A.getElement(i));
    	}
    }
    public static void main (String args []) throws Exception{
    	myQueueUsingDynamicArray B = new myQueueUsingDynamicArray(0);
    	B.enqueue(1);B.enqueue(5);B.dequeue();B.dequeue();B.dequeue();
    	B.display();
    }
    
    
}
