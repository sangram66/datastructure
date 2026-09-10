'''
Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
Example 4:

Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can pick from trees [1,2,1,1,2].
 '''

class Solution(object): 
    def totalFruit(self, tree):
        seen, runningMax, start, rmv = {}, 0, 0, None
        for i, fruit in enumerate(tree):
            if fruit in seen or len(seen) < 2:
                print ("seen:"+str(seen))
                runningMax = max(runningMax, i-start+1)
                print ("runningMax:"+str(runningMax))
            else:
                for s in seen.keys(): 
                    if s != tree[i-1]: rmv = s
                start = seen[rmv] + 1
                print ("seen before remove:"+str(seen))
                del seen[rmv]
                print ("seen after remove:"+str(seen))
            seen[fruit] = i
        return runningMax
    
    
print (Solution().totalFruit([1,2,3,2,2,5]))