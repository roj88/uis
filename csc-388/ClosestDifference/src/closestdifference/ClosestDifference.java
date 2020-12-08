/*
 * filename: ClosestDifference.java
 * @author: Roland Carter
 * date: 2020-11-01
 * purpose: csc 388 ClosestDifference assignment
 */
package closestdifference;

// import libraries
import java.io.*;
import static java.util.Objects.isNull;


// linked list Node class 
class Node {
    // data is the data inserted into the list, and Node
    // connects the data
    int data; 
    Node next; 

    // default constructor for new nodes
    Node(int data) {
        this.data = data;
    } 
} // end 


// class LinkedList implements singly linked list
class LinkedList {
    // define head (beginning) and tail (end) of list
    // note: there is no default contructor since it is not needed
    public Node head, tail = null;

    // putAtTail places new data at the end of a linked in
    public void addToTail(int data){
        // checks if linked list is empty
        // if it is, then create a new head node and place
        // head and tail as equal
        if(head == null){
            head = new Node(data);
            tail = head;
            return;
        }

        // when list is nonempty, we add the new node to the tail
        // and change the reference to tail to point to the newly added node
        tail.next = new Node (data);
        tail = tail.next;
    }
    
    public String toString() {
        // initiate empty string to hold result
        String res = "";
        
        // start at current head in LinkedList
        Node current = head;
        
        // iterate over LL until there are no more indices
        while(current != null){
            res += current.data;
            if(current.next != null){
                res += ", ";
            }
            current = current.next;
        }
        return res;
    }
    
    public int linkedListSum() {
        int sum = 0;
        Node h = head;
        while(h != null) {
            sum += h.data;
            h = h.next;
        }
        return sum;
    }
}

public class ClosestDifference {    
    // readFileIntoLinkedList is a static method that places the data from the
    // in.txt file into the LinkedList
    public static void readFileIntoLinkedList(LinkedList l) throws IOException{
        // define file name (relative to 
        File file = new File ("in.txt");

        // create new BufferedReader object
        BufferedReader br = new BufferedReader(new FileReader(file));

        // declare variable to ingest string from file
        String line =  null;

        // read single line of text into string
        line = br.readLine();
        
        // tokenize input into an array of strings (will be converted
        // the ints)
        String[] stringArray = line.split(" ");
        
        // place each index into LinkedList object in order
        for(int i = 0; i < stringArray.length; i++) {
            // convert string to int and place into Node.data
            int data = Integer.parseInt(stringArray[i]);
            
            // add data to the LinkedList object
            l.addToTail(data);
        }
    }
    
    // findMinimumDifference is a static method that recursively traverses a
    // singly linked list in order to find the minimum sum of list
    // partitions
    public static int findClosestDiff(Node head, int currentSum, int totalSum) {
    // since this is recursive, there is a base condition
    // in this case that condition is when there is no head
    // associated with the next node
    if (isNull(head)) {
        return Math.abs((totalSum - currentSum) - currentSum);
    }

    // return the minimum absolute value between two recursive
    // calls of root Nodes
    return Math.min(findClosestDiff(head.next, currentSum + head.data, totalSum),
            findClosestDiff(head.next, currentSum, totalSum));
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        // variable to hold the ClosestDifference
        int closestDiff;
        String ans;
        
        // initiate new LinkedList instance
        LinkedList llist = new LinkedList();
        
        // read file into new LinkedList instance
        readFileIntoLinkedList(llist);

        // get the closest difference
        closestDiff = findClosestDiff(llist.head, 0, llist.linkedListSum());
        
        // print out the answer
        ans = String.format("The Closest Diff of the LinkedList: {%1$s} is %2$s",
                llist.toString(),
                closestDiff);
        System.out.println (ans);
    }
}
