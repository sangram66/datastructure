#https://leetcode.com/explore/interview/card/apple/351/design/3139/
class NestedIterator:
    
    def __init__(self, nestedList):
        def flatten_list(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self._integers.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList()) 
        self._integers = []
        self._position = -1 # Pointer to previous returned.
        flatten_list(nestedList)
    
    def next(self) :
        self._position += 1
        return self._integers[self._position]
        
    def hasNext(self) :
        return self._position + 1 < len(self._integers)
    
    
