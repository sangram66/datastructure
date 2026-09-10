'''
https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/description/
You are given positive integers low, high, and k.

A number is beautiful if it meets both of the following conditions:

The count of even digits in the number is equal to the count of odd digits.
The number is divisible by k.
Return the number of beautiful integers in the range [low, high].

Input: low = 10, high = 20, k = 3
Output: 2
Explanation: There are 2 beautiful integers in the given range: [12,18].
- 12 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
- 18 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
Additionally we can see that:
- 16 is not beautiful because it is not divisible by k = 3.
- 15 is not beautiful because it does not contain equal counts even and odd digits.
It can be shown that there are only 2 beautiful integers in the given range.

'''

'''
class Solution(object):
    def check_beautiful(self,num,k):
        if num % k != 0 :
            return False
        od=ev=0
        for val in str(num):
            if int(val) %2 != 0:
                od += 1
            else:
                ev += 1

        return od == ev


    def count_beautiful_inetegers(self,low,high,k):
        count =0
        for num in range(low,high+1):
            if self.check_beautiful(num,k):
                count += 1

        return count

if __name__ == "__main__":
    sol=Solution()
    low = 10
    high = 20
    k = 3
    print (sol.count_beautiful_inetegers(low,high,k))
'''

class Solution:
    def check_beautiful(self, num, k):
        if num % k != 0:
            return False

        digits = list(map(int, str(num)))
        return sum(d % 2 != 0 for d in digits) == sum(d % 2 == 0 for d in digits)

    def count_beautiful_integers(self, low, high, k):
        return sum(1 for num in range(low, high + 1) if self.check_beautiful(num, k))

if __name__ == "__main__":
    sol = Solution()
    low, high, k = 10, 20, 3
    print(sol.count_beautiful_integers(low, high, k))


'''
Time Complexity: O(n * d)
Space Complexity: O(d) (excluding input storage)
'''

