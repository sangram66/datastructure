'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''
'''
class Solution:
    def mergeKLists(self, lists) :
        if not lists or len(lists)==0: return None
        
        def mergeTwoLists(list1, list2):
            dummy = ListNode(0, None)
            prev, tmp = dummy, None
            while list1 and list2:
                if list1.val < list2.val:
                    tmp = list1.next
                    prev.next = list1
                    list1 = tmp
                else:
                    tmp = list2.next
                    prev.next = list2
                    list2 = tmp
                prev = prev.next
            if list1:
                prev.next = list1
            if list2:
                prev.next = list2
            return dummy.next
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                mergedList = mergeTwoLists(list1, list2)
                mergedLists.append(mergedList)
            lists = mergedLists
        
        return lists[0]
'''   
class Node(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None
        
    def printList(self,node):
        while (node != None):
            print(node.data,end = " ")
        node = node.next
class Solution:
    def mergeTwoLists(self,list1, list2):
        dummy = temp= Node()
        while list1 and list2:
            if list1.val < list2.val:
                temp.next= list1
                list1=list1.next
            else:
                temp.next= list2
                list2=list2.next
            temp=temp.next
        temp.next=list1 or list2
        return dummy.next

    def mergeKLists(self, lists):
        if not lists or len(lists)==0: return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                mergedList = self.mergeTwoLists(list1, list2)
                mergedLists.append(mergedList)
            lists = mergedLists
        
        return lists[0] 

if __name__=="__main__":
    sol=Solution()
    # Number of linked
    # lists
    k = 3
     
    # Number of elements
    # in each list
    n = 4
 
    # an array of pointers
    # storing the head nodes
    # of the linked lists
    arr = [None for i in range(k)]
 
    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)
 
    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)
 
    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)
    head = sol.mergeKLists(arr)
    
    head.printList()

    