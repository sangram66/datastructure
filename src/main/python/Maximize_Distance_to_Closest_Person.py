'''
849. Maximize Distance to Closest Person
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

'''
class Solution:
    def maxDistToClosest(self, seats):
        L = len(seats)
        
        # 1) Get seat of each person
        # e.g seats = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]
        #     S = [1, 5, 7]
        S = [i for i in range(L) if seats[i]]
        
        # 2) Calculate distance between two sequential person
        #    S = [1, 5, 7]
        #    d = [(5-1//2)=2, (7-5)//2=1] = [2, 1]
        d = [S[i+1]-S[i] for i in range(len(S)-1)] if len(S) > 1 else [0]
        
        # 3) Find maximum distance
        #    max( 
        #           sit between people,    # max([2, 1]) // 2 = 1
        #           sit in the beginning,  # [2, 1, 0, 0, 0, ..., 1, 0, 0] -> First 2 and second 1 with distance S[0]
        #           sit in the end,        # [0, 1, 0, 0, 0, ..., 1, 0, 2] -> Last 2 and last 1 with distance 2 
        #       )
        return max(max(d)//2, S[0], L-1-S[-1])
    
if __name__=="__main__":
    seats = [1,0,0,0,1,0,0,0,0,1]
    sol=Solution()
    print (sol.maxDistToClosest(seats))




'''
Solution -2 
class Solution(object):
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        print (list(i for i, seat in enumerate(seats) if seat))
        prev, future = None, next(people)
        print (prev, future)

        ans = 0
        print (list(enumerate(seats)))
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                print (left,right)
                ans = max(ans, min(left, right))
                print (ans)

        return ans
''' 
'''
import math
class Solution:
    def maxDistToClosest(self, seats):
        
        if len(seats)<=2:
            return 1
        
        p1,p2,maxZeros,conZero=0,0,0,0
        
        while p2<len(seats):
            
            if seats[p1]==0 and seats[p2]==0:
                    conZero=p2-p1+1
                    maxZeros=max(maxZeros,conZero) if p1==0 or p2==len(seats)-1 else max(maxZeros,math.ceil(conZero/2))
                    p2+=1
                    
            elif seats[p1]==1 and seats[p2]==1:
                    p1,p2=p2,p2+1
                    
            elif seats[p1]!=seats[p2]:
                    conZero=abs(p2-p1)
                    maxZeros=max(maxZeros,conZero) if p2==len(seats)-1 else max(maxZeros,math.ceil(conZero/2))
                    p1=p2 if seats[p2]==1 else p1 #ie: exchange pointers in the next iter if p1 is free and p2 is occupied
                    p2=p2+1
            
        return maxZeros  
        
import itertools 
import math
class Solution(object):
    def maxDistToClosest(self, seats):
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans,seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, math.ceil((K+1)/2))

        return ans
 ''' 
