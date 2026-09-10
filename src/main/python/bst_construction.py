# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
import unittest
class main_BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentnode=self
        while True :
            if value < currentnode.value:
                if currentnode.left is None:
                    currentnode.left = main_BST(value)
                    break
                else:
                    currentnode = currentnode.left
            else:
                if currentnode.right is None:
                    currentnode.right = main_BST(value)
                    break
                else:
                    currentnode = currentnode.right 
        return self

    def contains(self, value):
        # Write your code here.
        currentnode=self
        while currentnode is not None:
            if value < currentnode.value:
                currentnode = currentnode.left
            elif value > currentnode.value:
                currentnode=currentnode.right
            else:
                return True
        return False
            

    def remove(self, value,parentnode=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentnode=self
        while currentnode is not None:
            if value < currentnode.value:
                parentnode=currentnode
                currentnode=currentnode.left
            elif value > currentnode.value:
                parentnode=currentnode
                currentnode=currentnode.right
            else:
                if currentnode.left is not None and currentnode.right is not None:
                    currentnode.value = currentnode.right.getminvalue()
                    currentnode.right.remove(currentnode.value,currentnode)
                elif parentnode is None:
                    if currentnode.left is not None:
                        currentnode.value=currentnode.left.value
                        currentnode.right=currentnode.left.right
                        currentnode.left=currentnode.left.left
                    elif currentnode.right is not None:
                        currentnode.value=currentnode.right.value
                        currentnode.left=currentnode.right.left
                        currentnode.right=currentnode.right.right
                    else:
                        pass
                elif parentnode.left == currentnode:
                    parentnode.left = currentnode.left if currentnode.left is not None else currentnode.right
                elif parentnode.right == currentnode:
                    parentnode.right = currentnode.left if currentnode.left is not None else currentnode.right
                break
        return self 
    
    def getminvalue(self):
        currentnode=self
        while currentnode.left is not None:
            currentnode=currentnode.left
        return currentnode.value

    def display(self):
        lines,*_ = self._display_aux()
        for line in lines:
            print(line)
            
    def levelOrder(self):
        root=self
        if not root:
            return []
        ans = []
        queue = [(root, 0)]
        cur, curDepth = [], 0
        while queue:
            node, depth = queue.pop(0)
            print ("node, depth,curDepth: "+str(node.value),str(depth),str(curDepth))
            if curDepth != depth:
                ans.append(cur)
                cur = []
                curDepth += 1
            cur.append(node.value)
            print ("cur : "+str(cur))
            print ("ans : "+str(ans))
            if node.left:
                print ("left")
                queue.append((node.left, depth+1))
            if node.right:
                print ("right")                
                queue.append((node.right, depth+1))
        ans.append(cur)  #add back the last level of nodes
        print (ans)    
        print ("depth :"+str(curDepth))
                
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    
def brachsums(root):
    sums=[]
    calculateBranchSums(root,0,sums)
    return sums

def calculateBranchSums(node,runningsum,sums):
    if node is None:
        return 
    
    newrunningsum = runningsum + node.value
    if node.left is None and node.right is None:
        sums.append(newrunningsum)
        return 
    
    calculateBranchSums(node.left,newrunningsum,sums)
    calculateBranchSums(node.right,newrunningsum,sums)

root = main_BST(10)
root.left = main_BST(5)
root.left.left = main_BST(2)
root.left.left.left = main_BST(1)
root.left.right = main_BST(5)
root.right = main_BST(15)
root.right.left = main_BST(13)
root.right.left.right = main_BST(14)
root.right.right = main_BST(22)
#root.display()
root.insert(12)
#root.display()
root.remove(10)
root.display()
#print(root.getminvalue())
#print (brachsums(root))
root.levelOrder()

'''
if __name__=='__main__':
    print("hello1")
    
    BST=main_BST()
    root = BST(10)
    
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    print (BST)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))
'''