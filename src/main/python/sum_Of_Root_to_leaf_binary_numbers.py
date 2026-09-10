'''
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/?envType=problem-list-v2&envId=tree

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.



Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0


'''

# 1. Define what a Tree Node looks like in memory
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 2. Your original solution class
class Solution:
    def sumRootToLeaf(self, root):

        def dfs(node, current):
            if not node:
                return 0

            # Build binary number
            current = current * 2 + node.val

            # If leaf node
            if not node.left and not node.right:
                return current

            # Return sum of left and right subtree
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)
# 3. The Entry Point to run the code in IntelliJ
if __name__ == "__main__":
    # Manually construct the tree from your previous example:
    #       1
    #      / \
    #     0   1
    #   / \  /  \
    #  0   1 0   1
    tree_root = TreeNode(1)
    tree_root.left = TreeNode(0)
    tree_root.right = TreeNode(1)
    tree_root.left.left = TreeNode(0)
    tree_root.left.right = TreeNode(1)
    tree_root.right.left = TreeNode(0)
    tree_root.right.right = TreeNode(1)

    # Create the object instance
    solver = Solution()

    # Run the function and capture the return value
    total_sum = solver.sumRootToLeaf(tree_root)

    # Print the result to the IntelliJ console
    print(f"The total sum of root-to-leaf paths is: {total_sum}")