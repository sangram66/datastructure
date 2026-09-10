class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
            print (self.min_stack[-1])

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None

        ans = self.stack.pop()
        if ans == self.min_stack[-1]:
            self.min_stack.pop()

        return ans

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return None
        print (self.min_stack[-1])
        return self.min_stack[-1]
        
    
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
print(obj.top())
print(obj.pop())

