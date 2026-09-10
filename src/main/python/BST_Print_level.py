class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        queue = [(root, 0)]
        cur, curDepth = [], 0
        while queue:
            node, depth = queue.pop(0)
            print (curDepth,depth)
            if curDepth != depth:
                ans.append(cur)
                cur = []
                curDepth += 1
            cur.append(node.val)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        ans.append(cur)  #add back the last level of nodes
        return ans
    
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print (Solution().levelOrder(root))
