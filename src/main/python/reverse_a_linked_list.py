'''

  Write a function that takes in the head of a Singly Linked List, reverses the
  list in place (i.e., doesn't create a brand new list), and returns its new head.


  Each  LinkedList node has an integer  value as well as a  next node pointing to the next node in the list or to None
 if it's the tail of the list.


  You can assume that the input Linked List will always have at least one node; in other
  words, the head will never be None
  
sample input 
head =0 -> 1 ->  2 ->  3 ->  4 ->  5    //head is 0
sample output 

0 <- 1 <-  2 <-  3 <-  4 <-  5  //head is 5
'''
'''
def reverselinklist(head):
    p1,p2=None,head
    while p2 is not None:
        p3=p2.next
        p2.next=p1
        p1=p2
        p2=p3
    return p1
'''
# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None
  
    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
  
    # print method for the linked list
    def printLL(self):
        print ("\t")
        current = self.head
        while(current):
            print(current.data , end = " ")
            current = current.next
      
    def reverselinklist(self):
        p1,p2=None,self.head
        while p2 is not None:
            p3=p2.next
            print (p2.next)
            p2.next=p1
            p1=p2
            p2=p3
        self.head=p1     


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
LL.reverselinklist()
LL.printLL()