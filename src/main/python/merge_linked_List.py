# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.val = value
        self.next = None
    
    def print_list(self):
         p = self
         while True:
             print(p.val, end='')
             p = p.next
             if not p:
                 break
             else:
                 print("--> ", end='')
         print()

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tail=dummy=LinkedList(0)
        while True:
            if l1 is None:
                tail.next=l2
                break
            if l2 is None:
                tail.next=l1
                break
                
            if l1.val < l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
                
            tail = tail.next 
        return dummy.next            
    
    

a=LinkedList(2)
b=LinkedList(3)
c=LinkedList(10)

a.next = b
b.next = c
print("List 1: ")
a.print_list()
    
aa=LinkedList(1)
bb=LinkedList(3)
cc=LinkedList(4)

aa.next = bb
bb.next = cc
print("List 2: ")
aa.print_list()

merged = Solution().mergeTwoLists(a, aa)
print (merged)
if merged:
    merged.print_list()

