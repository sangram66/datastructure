# Python3 code
class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        s=[]
        for i in range(len(arr)):
            while s and s[-1].get("value") < arr[i]:
                d = s.pop()
                print ("inside while: "+str(d))
                arr[d["ind"]] = arr[i]
                print (arr)
            s.append({"value": arr[i], "ind": i})
            print ("s:"+str(s))
            
        print (arr)
        print (s)
        while s:
            d = s.pop()
            arr[d["ind"]] = -1
        return arr
         
if __name__ == "__main__":
    print(Solution().nextLargerElement([6,2,0,1,3,8],6))