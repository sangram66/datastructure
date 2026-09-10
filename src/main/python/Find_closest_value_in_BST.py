'''
Find Closest Value In BST
 You are given a BST data structure consisting of BST nodes. 
 Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. 
 A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. You are also given a target integer value; write a function that finds the closest value to that target value contained in the BST. Assume that there will only be one closest value.
'''
'''
#Most Optimized sol  -- Iterative Soln 
#Average : time- O(log(n)) | space: O(1) 
#worst : time- O(n)) | space: O(1)  -- When the BST is single chain and the value is at end 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:

                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None :
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value :
            currentNode = currentNode.left
        elif target > currentNode.value :
            currentNode = currentNode.right
        else:
            break
    return closest     
    
test = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
.insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
.insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
.insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)

print (test)
test1=findClosestValueInBst(test,4502)
print (test1)
'''


#Most Optimized sol  -- recursive Soln 
#Average : time- O(log(n)) | space: O(log(n))-- because of the frame we call recursively , since it is called recursive it stores some memory for each recursive call
#worst : time- O(n)) | space: O(n)  -- When the BST is single chain and the value is at end 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:

                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) >= abs(target - tree.value):
        closest = tree.value
    if target < tree.value :
        return findClosestValueInBstHelper(tree.left,target,closest)
    elif target > tree.value :
        return findClosestValueInBstHelper(tree.right,target,closest)
    else:
        return closest    
    
test = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
.insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
.insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
.insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)

print (test)
test1=findClosestValueInBst(test,20)
print (test1)