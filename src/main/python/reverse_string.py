'''

https://leetcode.com/problems/reverse-string/description/?envType=company&envId=apple&favoriteSlug=apple-three-months
344. Reverse String
Easy

Topics

Companies

Hint
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

from typing import List
class Solution:
    def reverse_string(self, s: List[str]) -> None:
        def helper(left,right):
            if left > right :
                print (s)
                return
            s[left], s[right] = s[right] , s[left]
            helper(left+1, right-1)
        helper(0,len(s)-1)

if __name__ == "__main__":
    sol = Solution()
    s = ["h","e","l","l","o"]
    print (sol.reverse_string(s))

