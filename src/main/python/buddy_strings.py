'''
https://leetcode.com/problems/buddy-strings/description/

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Idea

Using 2 indices diff1, diff2 to store up to 2 different places between string A and string B.
If there are more than 2 different places -> Invalid.
If there are 2 different places -> Compare A[diff1] vs B[diff2] and A[diff2] vs B[diff1].
If there is only 1 different places -> Invalid.
If no difference between A and B then check if A contains at least 1 duplicate letters so that we can swap them.
Example 1: A = "ab", B = "ab"
Example 2: A = "aab", B = "aab",

Complexity:

Time: O(N)
Space: O(26), A_letters stores up to 26 characters

'''
class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        diff1, diff2 = -1, -1
        A_letters = set()
        for i in range(len(A)):
            if A[i] != B[i]:
                if diff1 == -1:
                    diff1 = i
                elif diff2 == -1:
                    diff2 = i
                else:
                    return False # More than 2 different places between A & B
            A_letters.add(A[i])
        if diff1 != -1 and diff2 != -1: # There are 2 different places
            return A[diff1] == B[diff2] and A[diff2] == B[diff1]
        if diff1 != -1: # Only have 1 different place
            return False
        return len(A_letters) < len(A) # No different between A & B, check if A contains at least 1 duplicate letters.