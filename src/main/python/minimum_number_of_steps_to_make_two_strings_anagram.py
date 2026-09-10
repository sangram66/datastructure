'''
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.
-- Mark the words , make T anagram of S , not vice versa

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.



Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.



crux
If both strings have the same number of that character → count all of them.
If numbers are different → count the minimum number (since only those are actually matching).

You always match as many letters as possible (the smaller count between s and t) for each letter, and then the unmatched letters tell you how many steps are needed.




Brute Force
Time complexity:
O(n)

Space complexity:
O(1)
'''


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        smp = {}
        tmp = {}
        cnt = 0

        for a in s:
            smp[a] = smp.get(a, 0) + 1

        for a in t:
            tmp[a] = tmp.get(a, 0) + 1

        for key, value in smp.items():
            if key in tmp:
                if value == tmp[key]:
                    cnt += value
                else:
                    cnt += min(value, tmp[key])

        return len(s) - cnt



s = "leetcode"
t = "practice"
print (Solution().minSteps(s,t))