""" 
class Solution:
    def groupAnagrams(self, strs):

        ret = []  # return list[]
        dic = {}  # dictionary { [sorted str]:  cooresponding list index need to write in}
        idx = 0 # index of the list, should be update whenever detects a new key
        for str in strs:
            key = ''.join(sorted(str)) # sort individual element in order
            print ("key --> "+key)
            print (dic)
            if key in dic:
                ret[dic[key]].append(str) #ret[idx].append(str)
                print (ret)
                print(str, idx, ret[idx - 1]) #you may check how code runs by printing out ret[idx] list
            else:
                ret.append([str])  
                dic[key] = idx
                print ("dic")
                print (dic)
                idx += 1 # update key value whenever there is a new key written into dictionary
            
        return ret  

sol=Solution()
#wordArr = ["eat", "tea", "tan", "ate", "nat", "bat"]
wordArr = ["abc", "dabd", "bca", "cab", "ddba"]
size = len(wordArr) 
print (sol.groupAnagrams(wordArr))

    
"""   
'''
class Solution:
    def groupAnagrams(self, strs) :
        dic = {}
        for x in strs:
            print ("string -> "+x)
            h = 1
            for c in x:
                h += hash(c) # actually, I use '*' here at first, but I found '+' work better
            if h not in dic:
                dic[h] = [x]
            else:
                dic[h].append(x)
            
            print (dic)
        return list(dic.values())
sol=Solution()
wordArr = ["abc", "dabd", "bca", "cab", "ddba"]
size = len(wordArr) 
print (sol.groupAnagrams(wordArr))
'''

#time= O(W*N*log(n))  
#space= O(W*N)
# w= number of the word
# n = length of word
def groupAnagrams(words):
    # Write your code here.
    anagram={}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword in anagram:
            anagram[sortedword].append(word)
        else:
            anagram[sortedword] = [word]
    return list(anagram.values())
wordArr = ["abc", "dabd", "bca", "cab", "ddba"]
print (groupAnagrams(wordArr))