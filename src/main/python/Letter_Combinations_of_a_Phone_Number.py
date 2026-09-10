
'''

https://leetcode.com/explore/interview/card/amazon/84/recursion/521/

Question 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]




Time complexity: O ( 4^N ⋅ N ) , where N N is the length of digits. Note that 4 in this expression is referring to the maximum value length in the hash map,
 and not to the length of the input.  The worst-case is where the input consists of only 7s and 9s. 
 In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to N N to build the combination. This problem can be generalized to a scenario where numbers correspond with up to M M digits, in which case the time complexity would be O ( M^N ⋅ N )  For the problem constraints, we're given, M = 4 M=4, because of digits 7 and 9 having 4 letters each.

Space complexity:  O(N), where  N N is the length of digits.  Not counting space used for the output, 
the extra space we use relative to input size is the space occupied by the recursion call stack. 
It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.  
As the hash map does not grow as the inputs grows, it occupies  O(1) space.


'''



'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        s = []
        for ch in digits:
            if ch in digits:
                s.append(ch)
        print ("s : "+str(s))
        if not s:
            return []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        # 
        def dfs(s, i, path, res):
            if i==len(s):
                res.append(path)
                print ("inside if res ::-------------------------- :"+str(res))
                return
            else:
                lst = dic[s[i]]
                print ("inside else lst:"+str(lst))
                for j in range(len(lst)):
                    print("j :"+str(j))
                    print ("inside else s, i+1, path, lst[j], res:  "+str(s) +','+str(i+1) +','+str(path)+','+str(lst[j])+','+str(res))
                    dfs(s, i+1, path+lst[j], res)
        # 
        dfs(s, 0, '', res)
        return res
'''
'''
class Solution:
    def letterCombinations(self, digits):
        keywords = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        if len(digits) == 0: return []
        
        def recurse(digits):
            if len(digits) == 1: return [key for key in keywords[int(digits)]]
            else:
                l1 = [key for key in keywords[int(digits[0])]]
                l2 = recurse(digits[1:])
                return [a+b for a in l1 for b in l2]
            
        return recurse(digits)
           
Input= "234"    
print (Solution().letterCombinations(Input))
'''

class Solution:
    def letterCombinations(self, digits):
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0: 
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            print ("index:"+str(index))
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            print (possible_letters)
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                print (path)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()
                print (path)

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations
    

print (Solution().letterCombinations("23"))
