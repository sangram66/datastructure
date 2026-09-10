'''
class Solution:
    def maxProfit(self, prices: List[int]):
        minPrice = prices[0]
        maxPrice = prices[-1]
        currProfit = maxPrice - minPrice
        maxProfit = max(0, currProfit)
        
        for price in prices[1:-1]:
            if price < minPrice:
                minPrice = price
                maxPrice = prices[-1] #Invalidate any previously updated maxPrice.
                currProfit = maxPrice - minPrice
                maxProfit = max(currProfit, maxProfit)
            
            if price > maxPrice:
                maxPrice = price
                currProfit = maxPrice - minPrice
                maxProfit = max(currProfit, maxProfit)
        
        return maxProfit
        

A= [7,1,5,3,6,4]           
print (Solution().maxProfit(A))
'''

def maxProfit( prices) :
    minu = prices[0]
    maxp = 0
    for i in prices:
        minu = min(minu,i)
        currentp = i - minu
        if maxp < currentp:
            maxp = currentp
    return maxp

A= [7,1,5,3,6,4]           
print (maxProfit(A))