'''
  Write a function that takes in a Binary Search Tree (BST) and a target integer
  value and returns the closest value to that target value contained in the BST.
  
You can assume that there will only be one closest value

  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.


Each BST node has an integer value, a left child node, and a 
right child node. A node is said to be a valid 
BST node if and only if it satisfies the BST property: its 
value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; and its children nodes are either valid
BST nodes themselves or  None/ null.

Optimal Space & Time Complexity
Average: O(log(n)) time | O(1) space - where n is the number of nodes in the BST
Worst: O(n) time | O(1) space - where n is the number of nodes in the BST


'''
def findClosestValueinBst(tree,target):
    return findClosestValueinBsthelper(tree,target,float("inf"))

def findClosestValueinBsthelper(tree,target,closest):
    currentNode= tree
    while currentNode  is not None :
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left 
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break 
    return closest  

