class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class Solution:
    def __init__(self):
        self.head=None
    
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
               
    def addTwoNumbers(self, l1, l2):
        prev=None
        temp=None
        carry=0
        while (l1 is not None or l2 is not None):
            fdata=0 if l1 is None else l1.data
            sdata=0 if l2 is None else l2.data
            sum=carry+fdata+sdata
            print ("sum   :"+str(sum))
            
            carry=1 if sum>=10 else 0
            print ("carry1   :"+str(carry))
            sum=sum if sum<10 else sum%10
            print ("sum1   :"+str(sum))
            
            temp =Node(sum)
            
            if self.head is None:
                self.head=temp
            else:
                prev.next=temp
            
            prev=temp
            if l1 is not None: 
                l1 = l1.next
            if l2 is not None: 
                l2 = l2.next
        if carry > 0: 
            temp.next = Node(carry) 
            
    def printList(self): 
        temp = self.head 
        while(temp): 
            print ((temp.data),end='')
            temp = temp.next

if __name__=='__main__':
                 
    first = Solution() 
    second = Solution() 
  
# Create first list 
    first.push(3) 
    first.printList() 

    first.push(4) 
    first.printList() 
   
    first.push(2)
    first.printList() 
     
    #first.push(5) 
    #first.push(7) 
    print ("First List is ") 
    first.printList() 


# Create second list 
    second.push(4) 
    second.push(6)
    second.push(5)  
    #second.push(6) 
    print ("\nSecond List is ")
    second.printList() 
  
# Add the two lists and see result 
    res = Solution() 
    res.addTwoNumbers(first.head, second.head) 
    print ("\nResultant list is ") 
    res.printList() 
    
    
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempsum=0
        temp=ListNode(0)
        curr=temp
        carry=0
        while l1 or l2 or carry !=0:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            carry,out=divmod(val1+val2+carry,10)
            curr.next=ListNode(out)
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None 
        return (temp.next)
'''
              