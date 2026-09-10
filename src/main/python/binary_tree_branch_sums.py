'''
https://www.algoexpert.io/questions/Branch%20Sums
'''

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 
        
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self    
    
    def levelOrder(self):
        root=self
        if not root:
            return []
        ans = []
        queue = [(root, 0)]
        cur, curDepth = [], 0
        while queue:
            node, depth = queue.pop(0)
            if curDepth != depth:
                ans.append(cur)
                cur = []
                curDepth += 1
            cur.append(node.value)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        ans.append(cur)  #add back the last level of nodes
        print (ans)

    def display(self):
        lines,*_ = self._display_aux()
        for line in lines:
            print(line)
                
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
    #print (node.left,newrunningsum,sums)
    calculateBranchSums(node.left,newrunningsum,sums)
    #print ("moving to right")
    #print (node.right,newrunningsum,sums)
    calculateBranchSums(node.right,newrunningsum,sums)




           
root=BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
root.display()
print (brachsums(root))
root.levelOrder()