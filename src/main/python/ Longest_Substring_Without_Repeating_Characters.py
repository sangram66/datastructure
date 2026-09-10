#https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans, current_ans, accur_dic = 0, 0, {}
        for i in range(len(s)):
            print ("index,letter: "+str(i)+"  ,  "+str(s[i]))
            if s[i] in accur_dic:
                print ('inside if  current_ans: '+str(current_ans)+","+str(i)+","+str(accur_dic[s[i]]))
                current_ans = min(current_ans + 1, i - accur_dic[s[i]])
                print ('inside if  current_ans: '+str(current_ans))
            else:
                current_ans += 1
                print ('inside else  current_ans: '+str(current_ans))
            ans = max(current_ans, ans)
            print ('inside else ans: '+str(ans))
            accur_dic[s[i]] = i
            print (accur_dic)
        return ans
    
if __name__=='__main__':
    sol=Solution()
    #s="GEEKSFORGEEKS"
    s=""
    res=sol.lengthOfLongestSubstring(s)
    print (res)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longi=[0,0]
        vis={}
        start=0
        for i,char in enumerate(s):
            print ("char:"+char)
            if char in vis:
                start=max(start,vis[char]+1)
                print (vis)
                print (start)
            if longi[1]-longi[0] < i+1 - start:
                longi=[start,i+1]
                print ("a:"+str(longi))  

            vis[char]=i
        print( s[longi[0]:longi[1]]   )    
        return (longi[1]-longi[0])

sol=Solution()
s="abcabcabd"
print(sol.lengthOfLongestSubstring(s))
