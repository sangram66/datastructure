''''
#https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/345/
#https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/345/discuss/279533/Simple-Python-with-explanation

from collections import defaultdict
class Solution:
    def minWindow(self, s, t) :
        
        if not s or not t or len(t) > len(s):
            return ""
        
        t_dict = defaultdict(int)
        for ch in t:
            t_dict[ch] += 1
        desired_count = len(t_dict)
        print ("desired_count : "+str(desired_count) )
        print ("tdict : "+str(list(t_dict)) )
        left = 0
        right = 0
        match_counter = 0
        res = ""
        min_len = len(s) + 1
        window_dict = defaultdict(int)
        print ("window_dict : "+str(list(window_dict)) )
        while right < len(s):
            print ("while right < len(s), right, len(s) : "+str(right) +  ':' + str(len(s)) )
            window_dict[s[right]] += 1
            print ("inside while window_dict : "+str(list(window_dict)) )
            if window_dict[s[right]] == t_dict[s[right]]:
                print ("inside while window_dict[s[right]] , t_dict[s[right]]: "+str(window_dict[s[right]])+" ," +str(t_dict[s[right]]) )
                match_counter += 1
            
            # Enter the following loop only when window has all required elements
            while match_counter == desired_count:
                print ("inside while match_counter, desired_count : "+str(match_counter) +  ':' + str(desired_count))
                #If length of current window is lesser update
                print ("min_len , right, left : "+str(min_len) +  ':' + str(right)+  ':' + str(left))
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    res = s[left:right + 1]
                    print ("res : "+str(res) )
                
                # Now lets contract the window, left pointer to contract, right pointer to expand
                window_dict[s[left]] -= 1
                print ("window_dict: t_dict "+str(window_dict)+ ':' +str(t_dict) )
                print ("window_dict[s[left]] : t_dict[s[left] "+str(window_dict[s[left]])+ ':' +str(t_dict[s[left]]) )
                # Check if the character removed from the left was part of t, if yes then match_counter should be updated
                print ("t_dict : "+str(t_dict) )
                if window_dict[s[left]] < t_dict[s[left]]:
                    print ("match_counter :" +str(match_counter))
                    match_counter -= 1
                # increment the left pointer to reduce window size
                
                left += 1
                print ("left : "+str(left) )
                
            right += 1
            print ("right : "+str(right) )
        print ("res : "+str(res) )    
        return res
    
if __name__=='__main__':
    sol=Solution()   
    s = "DEBANC"
    k = "ABC"
    print (sol.minWindow(s,k))
    
'''''
import collections
class Solution(object):
    def minWindow(self, s, t) :
        i = j = 0
        hashmap = collections.Counter(t)
        count = len(hashmap)
        min_window_start = 0
        min_window_length = len(s)+1
    
        while j < len(s):
            if s[j] in hashmap:
                hashmap[s[j]] -= 1
                if hashmap[s[j]] == 0:
                    count -= 1
                
            if count > 0:
                j += 1
            
            
            elif count == 0:
                while count == 0:
                    if (j-i+1) < min_window_length:
                        min_window_length = j-i+1
                        min_window_start = i
                    if s[i] in hashmap:
                        hashmap[s[i]] += 1
                        if hashmap[s[i]] == 1:
                            count += 1
                    i += 1
            
                j += 1
                    
        if min_window_length == len(s)+1:
            return ""
        else:
            return s[min_window_start:min_window_start+min_window_length]
if __name__=='__main__':
    sol=Solution()   
    #s = "abcd$ef$axb$c$"
    #k = "$$abf"
    s = "ADOBECODEBANC"
    k = "ABC"
    #s = "acbbaca"
    #k = "aba"    
    print (sol.minWindow(s,k))    

