#https://leetcode.com/explore/interview/card/apple/344/array-and-strings/2018/

'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return -1
        
        if len(s)==1:
            return 0
        
        if len(set(s))==1:
            return -1
        orde=[]
        cnt_hsh={}
        for i in s:
            orde.append(i)
            print("ordee "+str(orde))
            cnt_hsh[i]=cnt_hsh.get(i, 0) + 1
            print("cnt_hsh "+str(cnt_hsh))
 
        for i,key in enumerate(orde):
            if cnt_hsh[key] == 1:
                return i
            
        return -1
        
if __name__=='__main__':
    sol=Solution()
    print (sol.firstUniqChar('aadadaad'))
'''    
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return -1
        if len(s)==1:
            return 0
        if len(set(s))==1:
            return -1
        hash_cnt={}
        for i in s:
            if i in hash_cnt:
                hash_cnt[i]+=1
            else:
                hash_cnt[i]=1
        print (hash_cnt)
            
        for i,val in enumerate(s):
            if hash_cnt[val]==1:
                return i
        return -1

if __name__=='__main__':
    sol=Solution()
    print (sol.firstUniqChar('aadadaad'))