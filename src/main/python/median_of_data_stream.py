from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_max = []  # stores numbers smaller than the median
        self.data_min = []  # stores numbers greater than the median
        self.data_size = 0


    def addNum(self, num: int) -> None:
        heappush(self.data_max, -num)
        temp = heappop(self.data_max)
        heappush(self.data_min, -temp)
        self.data_size += 1
        
        if len(self.data_min) - len(self.data_max) == 2:
            temp = heappop(self.data_min)
            heappush(self.data_max, -temp)
            
        print (self.data_max )
        print (self.data_min )


    def findMedian(self) -> float:
        if self.data_size%2 != 0:
            return self.data_min[0]

        return (self.data_min[0]+(-self.data_max[0])) / 2
    
    

med=MedianFinder()
med.addNum(1)
med.addNum(3)
med.addNum(2)
med.addNum(6)
med.addNum(8)
med.addNum(7)
print (med.findMedian())