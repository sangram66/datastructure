'''
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# def two_sum(arr,targ):
#     look_for = {}
#     a= list(enumerate(arr,1))
#     print(a)
#     for n,x in enumerate(arr,1):
#         try:
#             print ("inside try")
#             print ("n x "+str(n) +' '+str(x))
#             print (look_for)
#             print ("inside look_for")
#             print (look_for[x], n-1)
#             return look_for[x], n-1
#         except KeyError:
#             look_for.setdefault(targ - x,n-1)
#             '''
#             This method returns the key value available in the dictionary and 
#             if given key is not available then it will return provided default value.
#             dict = {'Name': 'Zara', 'Age': 7}
#             print "Value : %s" %  dict.setdefault('Age', None)
#             print "Value : %s" %  dict.setdefault('Sex', None)
#             Value : 7
#             Value : None
#             >>> dict
#             {'Age': 7, 'Name': 'Zara', 'Sex': None}
#             '''
#             print ("inside execpt")
#             print (look_for)
# 
# a = (2,15,1,7)
# t = 9
# print(two_sum(a,t))  # (1,2)

"""
a = (-3,4,3,90)
t = 0
print(two_sum(a,t))  # (1,3)
"""


"""
def twosum(arr,trg):

    # Numbers that are needed to meet the target will be stored here along with an index of a complementary number.
    wanted_nums={}
    
    # Interating through a list of numbers
    for i in range(len(arr)):
        # If number in wanted_nums it means we've got the sum!
        if arr[i] in wanted_nums:
            return [wanted_nums[arr[i]],i]
            
        # If not, we store the difference (so the number we seek) along with an index
        else:
            wanted_nums[trg - arr[i]]=i
            

"""
'''
#to get the element
#time= O(n^2) | space :O(1)
def findtwosum(array,tgt):
    array.sort()
    l=0
    r=len(array)-1
    while l < r :
        if array[l] + array[r] > tgt:
            r-=1
        elif array[l] + array[r] < tgt:
            l+=1
        elif array[l] + array[r] == tgt:
            return [array[l] , array[r]]
        else:
            return []
        
#a = [3,2,4]
#t = 6
a = [3,2,4,0,6]
t = 6
print(findtwosum(a,t))  # (1,2)

'''
#To get posotion of the elemnt 
class Solution:
    def twoSum(self, nums, target):
        visited = {}
        result = []
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in visited:
                result.append([visited[comp],i])
                #result.append([comp,nums[i]])
                #break
            else:
                visited[nums[i]] = i
                print (visited)
        return result
nums = [3,2,4,0,6]
target = 6           
print (Solution().twoSum(nums,target))
