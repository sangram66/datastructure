'''

You are given a string word and an array of strings forbidden.

A string is called valid if none of its substrings are present in forbidden.

Return the length of the longest valid substring of the string word.

A substring is a contiguous sequence of characters in a string, possibly empty.



Example 1:

Input: word = "cbaaaabc", forbidden = ["aaa","cb"]
Output: 4
Explanation: There are 11 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" and "aabc". The length of the longest valid substring is 4.
It can be shown that all other substrings contain either "aaa" or "cb" as a substring.
Example 2:

Input: word = "leetcode", forbidden = ["de","le","e"]
Output: 4
Explanation: There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.
It can be shown that all other substrings contain either "de", "le", or "e" as a substring.

'''
class Solution:
    def longestValidSubstring(self, word, forbidden) -> int:

        forbidden_set = set(forbidden)
        max_len_f = max(len(f) for f in forbidden)
        print ("max_len_f:"+str(max_len_f))

        left = 0
        result = 0

        for right in range(len(word)):
            print ("++++++++++inside first loop++++++++++")
            print ("right:"+str(right))
            # Check last few characters ending at 'right' (from max 10 steps back)
            for j in range(right, max(right - max_len_f, left - 1), -1):
                print ("--------inside second loop--------")
                print ("max:"+str(max(right - max_len_f, left - 1)))
                print ("right:"+str(right))
                print ("j:"+str(j))
                print ("word:"+word[j:right + 1])
                if word[j:right + 1] in forbidden_set:
                    print ("inside:"+word[j:right + 1])
                    print ("left before:"+str(left))
                    left = j + 1
                    print ("left after:"+str(left))
                    break
            result = max(result, right - left + 1)

        return result
word = "cbaaaabc"
forbidden = ["aaa","cb"]
print (Solution().longestValidSubstring(word,forbidden))