'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

'''



from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned):

        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumerate(paragraph):
            #1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                #print ('1-')
                #print (word_buffer)
                #print (p,len(paragraph))
                
                if p != len(paragraph)-1:
                    continue
                
            #2). at the end of one word or at the end of paragraph
            #print ('2-')
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                #print (word)
                if word not in banned_words:
                    word_count[word] +=1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                # reset the buffer for the next word
                word_buffer = []

        return ans
    
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print (Solution().mostCommonWord(paragraph,banned))
