"""
def primes(n): # simple Sieve of Eratosthenes 
    odds = range(3, n+1, 2)
    print (odds)
    sieve = set(sum([range(q*q, n+1, q+q) for q in odds],[]))
    print (sieve)
    print ([2] + [p for p in odds if p not in sieve])
    return [2] + [p for p in odds if p not in sieve]

print ("ans:")
primes(10)
"""
"""
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    print ("prime")
    print (prime)
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
            print (p)
            print (prime[p])
            # Update all multiples of p 
            print (range(p * 2, n+1, p))
            for i in range(p * 2, n+1, p): 
                print ("i :"+str(i))
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            print p, 
  
# driver program 
if __name__=='__main__': 
    n = 30
    print ("Following are the prime numbers smaller than or equal to: "+str(n))
    SieveOfEratosthenes(n) 
"""
"""
def prime(n):
    seive=[True for i in range(n+1)]
    p=2
    while (p*p <= n):
        if seive[p]==True:
            for i in range(p*2,n+1,p):
                seive[i]=False
            p+=1
        for p in range(2,n):
            if seive[p]:
                print p,
                
if __name__=='__main__':
    n=30
    prime(n)
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        seive = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n): 
            if (seive[p] == True): 
                for i in range(p * 2, n+1, p): 
                    seive[i] = False
            p += 1
      
        for p in range(2, n): 
            if seive[p]: 
                print p,

if __name__=='__main__':
    sol=Solution()
    sol.countPrimes(10)
         