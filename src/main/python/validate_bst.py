

'''
class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
 
class Solution(object):       
    def validateBst(self,tree):
        return self.validatebsthelper(tree,float("-inf"),float("inf"))

    def validatebsthelper(self,tree,minvalue,maxvalue):
        if tree is None:
            return True
        if tree.value >= maxvalue or tree.value <= minvalue:
            return False
        print ("calling left tree : "+str(minvalue),str(tree.value),str(tree.left or "NONE"))
        leftisvalid = self.validatebsthelper(tree.left,minvalue,tree.value)
        print ("calling right tree : "+str(tree.right or "NONE"),str(tree.value),str(maxvalue))
        rightisvalid = self.validatebsthelper(tree.right,tree.value,maxvalue)
        return leftisvalid and rightisvalid
        
root = BST(4) 
root.left = BST(2) 
root.right = BST(5) 
root.left.left = BST(1) 
root.left.right = BST(3)
sol=Solution()
print (sol.validateBst(root))
'''

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
def validateBst(tree):
    return validatebsthelper(tree,float("-inf"),float("inf"))

def validatebsthelper(tree,minvalue,maxvalue):
    if tree is None:
        return True
    if tree.value >= maxvalue or tree.value <= minvalue:
        return False
    print ("calling left tree : "+str(minvalue),str(tree.value),str(tree.left or "NONE"))
    leftisvalid = validatebsthelper(tree.left,minvalue,tree.value)
    print ("calling right tree : "+str(tree.right or "NONE"),str(tree.value),str(maxvalue))
    rightisvalid = validatebsthelper(tree.right,tree.value,maxvalue)
    return leftisvalid and rightisvalid
        
'''    
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
'''
root = BST(4) 
root.left = BST(2) 
root.right = BST(5) 
root.left.left = BST(1) 
root.left.right = BST(3)
    
print (validateBst(root))

'''
 

""" Program to check if a given Binary 
Tree is balanced like a Red-Black Tree """
  
# Helper function that allocates a new  
# node with the given data and None  
# left and right poers.                                  
class newNode:  
  
    # Construct to create a new node  
    def __init__(self, key):  
        self.data = key 
        self.left = None
        self.right = None
  
# Returns true if given tree is BST.  
def isBST(root, l = None, r = None):  
  
    # Base condition  
    if (root == None) : 
        return True
  
    # if left node exist then check it has  
    # correct data or not i.e. left node's data  
    # should be less than root's data  
    if (l != None and root.data <= l.data) : 
        return False
  
    # if right node exist then check it has  
    # correct data or not i.e. right node's data  
    # should be greater than root's data  
    if (r != None and root.data >= r.data) : 
        return False
  
    # check recursively for every node.  
    left = isBST(root.left, l, root)
    right = isBST(root.right, root, r)
    return left and right 
  
  
# Driver Code  
if __name__ == '__main__': 

    root = newNode(3)  
    root.left = newNode(2)  
    root.right = newNode(5)  
    root.right.left = newNode(1)  
    root.right.right = newNode(4)  

    root = newNode(10)
    root.left = newNode(5)
    root.left.left = newNode(2)
    root.left.left.left = newNode(1)
    root.left.right = newNode(5)
    root.right = newNode(15)
    root.right.left = newNode(13)
    root.right.left.right = newNode(14)
    root.right.right = newNode(22)
    #root.right.left.left = newNode(40) 

    root = newNode(4) 
    root.left = newNode(2) 
    root.right = newNode(5) 
    root.left.left = newNode(1) 
    root.left.right = newNode(3)
    if (isBST(root,None,None)): 
        print("Is BST") 
    else: 
        print("Not a BST") 
'''