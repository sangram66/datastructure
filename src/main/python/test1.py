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
def longest(s,k):
    long=[0,1]
    freq=Counter()
    start=0
    longseencnt=0

    for i, char in enumerate(s):
        freq[char]+=1
        while len(freq) > k:
            start_char = s[start]
            freq[start_char]-=1
            if freq[start_char]==0:
                del freq[start_char]
            start+=1

        window=i+1-start
        if  longseencnt < window:
            longseencnt=max(longseencnt,window)
            long=[start,i+1]

    print(s[long[0]:long[1]])

    return longseencnt
s = "aa"
k = 1
print (longest(s,k))


