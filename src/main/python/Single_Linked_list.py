class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data, end=" ")
            temp = temp.next

    def insert(self,data):
        newnode = Node(data)
        current = self.head
        if current:
            while(current.next):
                current = current.next
            current.next = newnode
        else:
            self.head=newnode 

                
    def push_to_head(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print ("The node given should exist in Linkedlist")
            return        
        new_node = Node(new_data) 
        new_node.next = prev_node.next    
        prev_node.next = new_node
        
    def add_to_last(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while (last.next):
            last=last.next
            
        last.next = new_node
    
    def delete_node(self,key):
        temp=self.head
        if (temp is not None):
            if (temp.data==key):
                self.head=temp.next
                temp=None
                return
            
        while (temp is not None):
            if (temp.data==key): 
                break
            prev=temp
            temp=temp.next
            
        
        
        
if __name__=='__main__':
    llist = LinkedList()
    '''
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    second.next = third
    '''
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.printList()
    llist.push_to_head(4)
    print('\n')
    llist.printList()
    #llist.insertAfter(third,0)
    print('\n')
    llist.printList()
    llist.add_to_last(5)
    print('\n')
    llist.printList()
    
    
        