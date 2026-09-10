'''
340. Longest Substring with At Most K Distinct Characters
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

'''

from collections import Counter
class Solution:
    
    def lengthOfLongestSubstringKDistinct(self, string, numDistinctCharacters) :
        
        # create a counter that will store the frequency of characters
        freq = Counter()
        longi=[0,0]
        # create a variable to store the index of the left side of the window
        window_start = 0
        
        # create a variable to return that will hold the length of the longest valid substring seen
        longest_valid_substring_seen = 0
        
        # iterate through the entire string, "window_end" represents the "right side" of the window
        for window_end, char in enumerate(string):
            
            # load up the frequency counter until constraint violation
            freq[char] += 1
            
            # shrink the window if violates the constraint of more than the number of distinct characters
            # the length of the freq counter represents the number of distinct characters
            while len(freq) > numDistinctCharacters:
                
                # get the left char of the window (the char that window_start points to)
                left_char = string[window_start]
                
                # and decrement it in the counter
                freq[left_char] -= 1
                
                # IMPORTANT: we check the length of the frequency counter (which is equivalent to number of distinct chars)
                # we must delete chars that have a zero count, because we no longer have a distinct char in window
                if freq[left_char] == 0:
                    del freq[left_char]
                
                # shrink window here
                window_start += 1
            
            # valid window at this point, get the size of the window
            # and compare it to the longest valid substring seen so far
            # update longest_valid_substring_seen if we found a new longest valid substring
            window_size = window_end - window_start+1
            if window_size > longest_valid_substring_seen:
                longest_valid_substring_seen = max(longest_valid_substring_seen, window_size)
                longi=[window_start,window_end+1]
        print (string[longi[0]:longi[1]])
        return longest_valid_substring_seen
    
s = "aabacbebebe"
k = 3
print (Solution().lengthOfLongestSubstringKDistinct(s,k))