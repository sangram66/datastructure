
'''
Nth Fibonacci
The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.
Sample input: 6
Sample output: 5 (0, 1, 1, 2, 3, 5)
'''

'''
#Naive method, recursive call  
#O(n) time | O(n) space 
def getNthFib(n):
    if n ==2:
        return 1
    elseif n==1 :
        return 0
    else
       return  getNthFib(n-1)+getNthFib(n-2)    

print getNthFib(35)
'''




'''
#Memoization , recursive call  
#O(n) time | O(n) space 
def getNthFib(n,memoize = {1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n]=getNthFib(n-1, memoize)+getNthFib(n-2, memoize)
        return memoize[n]
    

print getNthFib(35)
'''


#just storing the last two calculation , iterative calls 
#O(n) time | O(1) space 
def getNthFib(n):
    lastTwo =[0,1]
    counter=3
    while counter <= n:
        nextFib = lastTwo[0]+lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter+=1
    return lastTwo[1] if n > 1 else lastTwo[0]


print getNthFib(2)

