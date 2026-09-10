# Clean Binary Search Code, O(N log Sum) time complexity, O(1) space
class Solution:
    def splitArray(self, A, m: int) -> int:
        lo,hi = max(A),sum(A) # lowest and highest value imaginable
        while lo<hi: # if lo==hi, there's nothing to be done
            mid = (hi+lo)//2 # Guessed max. sub-array value, check how many containers you actually need
            n, now = 1, 0 # n = numbers of containers ; now = value of current container
            for x in A:
                now += x
                if now>mid:
                    now  = x # Start new container
                    n   += 1
            if n<=m:
                hi = mid # "mid" was a valid answer, so we can bound "answer"<=mid (perhaps we can still get away with a lower threshold)
            else:
                lo = mid + 1 # "mid" was too small and produced too many containers, our answer is higher
        return lo
    
nums = [7,2,5,10,8]
m = 2
print (Solution().splitArray(nums,2))