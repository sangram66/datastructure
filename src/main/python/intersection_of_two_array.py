class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for i in nums2:
            d[i] = 1
        print(d)
        for j in nums1:
            if j in d:
                d[j] -= 1               # bcoz we donot want duplicate in final result
                print (d)
                if d[j] == 0:
                    res.append(j)
        return res 
    
nums1 = [9,4,9,8,4]
nums2 = [4,9,5]

print (Solution().intersection(nums1,nums2))