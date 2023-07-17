class myStackUsingDynamicArray{

    private dynamicArray A;
    //Other variables to be defined by student
    private int height;
    
    public myStackUsingDynamicArray(int height){
        A = new dynamicArray();
        height = 0;
        //Other initializations to be done by student
    }
    
    //This method should return the size of the stack
    public int getSize(){
        //To be written by student
    return	(height);
    }
    
    //This should implement the push operation of stack
    public void push(int value){
        //To be written by student
    	if (height==A.getSize()){
    		A.doubleSize();
    		try {
				A.modifyElement(value, height);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    		
    		height = height + 1; 
    		
    	}
    	else {
    		try {
				A.modifyElement(value,height);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    		height = height + 1;
    	}
    	 }
    
    //This should implement the pop operation of stack.
    //This method should throw an exception in case the stack is empty.
    public int pop() throws Exception {
        //To be written by student
    	if (height== 0){
    		System.out.println("stack is empty");
				throw new Exception();
    	}
    	else {
    int s = 0;
	try {
		s = A.getElement(height-1);
	} catch (Exception e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
    
		try {
			A.modifyElement(0, height-1);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    height = height - 1;
    if (height>0 && 2*height < A.getSize()){
    	A.halveSize();
    	return s;
    }
    else {
    	return s;
    }
    }
    }
   /* public void display () throws Exception{
    	for (int i = 0; i<=height-1;i++){
    		System.out.println(A.getElement(i));
    	}
    }
    public static void main (String args []) throws Exception{
    	myStackUsingDynamicArray B = new myStackUsingDynamicArray(0);
    	B.push(1); B.pop();B.push(54);
    	B.display();
    	
    }
    */
}