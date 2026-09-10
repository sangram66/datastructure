'''
349. Intersection of Two Arrays
Easy

440

854

Favorite

Share
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

#Binary search method
class Solution:
    def intersection(self, nums1, nums2) :
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        res = []
        nums1 = sorted(nums1)
        print ('nums1:'+str(nums1))
        nums2 = set(nums2)
        print ('nums2:'+str(nums2))
        for i in nums2:
            print ('i :'+str(i))
            l,r = 0,len(nums1)-1
            print ('l, r :'+str(l) + ' ' + str(r))
            while l <=r:
                m = (l+r)
                print ('m :'+str(m))
                if nums1[m] == i:
                    print ("nums1[m] :"+str(nums1[m]))
                    res.append(i)
                    print ("res :"+str(res))
                    break
                else:
                    if nums1[m] < i:
                        print ("nums1[m] < i:"+str(nums1[m]))
                        print ('l :'+str(l))
                        l = m + 1
                    else:
                        print ('r :'+str(r))
                        r = m - 1
        return res
'''
class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
'''    
if __name__=="__main__":
    sol=Solution()
    nums1 = [1, 4, 5, 6, 9, 10]
    nums2 = [9,4,9,8,4]
    #nums1 = [1,2,2,1]
    #nums2 = [2,2]    
    print (sol.intersection(nums1,nums2))