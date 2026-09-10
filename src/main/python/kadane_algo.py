# Write a function that takes a non empty array of integers amd return maximum sum that can be obtained by summing up all of the numbers in a non empty subarray of the input array. a subarray must only contain adjacent numbers
# sample input :[3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
# sample output :([1,3,-2,3,4,7,2,-9,6,3,1])

class Solution:
    def kadaneAlgo(self,array):
        maxHere = array[0]
        maxSofar = array[0]
        for num in array[1:]:
            maxHere = max(num,maxHere+num)
            maxSofar = max(maxHere,maxSofar)
        return maxSofar

if __name__ == '__main__':
    Sol=Solution()
    #Input= [-2,-1,-3,-4,-1,-2,-1,-5,-4]
    Input= [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
    print (Sol.kadaneAlgo(Input))