class solution():
    def longestsubstring(self,s):
        dic={}
        curr=0
        ans=0
        for i in range(0,len(s)):
            print ("string travessered so far: "+(s[:i]))
            print ("dictionary ")
            print (dic)
            print ("letter to be checked: "+s[i])
            if s[i] in dic:
                curr=max(curr+1,i-dic[s[i]])
            else:
                curr+=1
            ans=max(curr,ans)
            dic[s[i]]=i
        return (ans)
                
if __name__=='__main__':
    sol=solution()
    str="GEEKSFORGEEKS"
    print (str)
    print (sol.longestsubstring(str))