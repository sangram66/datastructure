from collections import deque
class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.uniques = deque([])
        self.dct = {}
        for num in nums:
            if num not in self.dct :
                self.uniques.append(num)
                self.dct[num] =1
            else:
                self.dct[num] +=1
    def showFirstUnique(self):
        """
        :rtype: int
        """
        rtn = -1
        isBreak = False
        if self.uniques :
            rtn = self.uniques.popleft()
            while rtn in self.dct and self.dct[rtn] > 1:
                if self.uniques:
                    rtn = self.uniques.popleft()
                else:
                    rtn = -1
                    isBreak = True
                    break
        else: return -1
        if not isBreak : self.uniques.appendleft(rtn)
        return rtn
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.dct :
            self.dct[value] =1
            self.uniques.append(value)
        else:
            self.dct[value] +=1
            
            

sol=FirstUnique([2,3,5])
print (sol.showFirstUnique())
sol.add(5)
print (sol.showFirstUnique())
sol.add(2)
print (sol.showFirstUnique())
sol.add(3)
print (sol.showFirstUnique())

