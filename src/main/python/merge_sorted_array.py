
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                print ("inside if:"+str(nums1))
            else:
                nums1[p] = nums2[p2]
                print ("inside else:"+str(nums1))
                p2 -= 1
                
 
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3               
Solution().merge(nums1,m,nums2,n)
print (nums1)
'''
def sortlists(s1,s2):
    res=[]*(len(s1)+len(s2))
    i=j=0
    while i < len(s1) and j < len(s2):
        
        if s1[i] < s2[j]:
            res.append(s1[i])
            i+=1
        else:
            res.append(s2[j])
            j+=1
            
    if i < len(s1):
        res+=s1[i+1:]
        
    elif j < len(s2):
        res+=s2[j+1:]
        
    return (res)
        
        
        
print (sortlists([1,2,4,6],[0,1,4,6,7,8]))
'''