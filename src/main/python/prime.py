def primes_method5(n):
    out = list()
    sieve = [True] * (n+1)
    print (sieve)
    for p in range(2, n+1):
        print (sieve[p])
        if (sieve[p] and sieve[p]%2==1 ):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out


print (primes_method5(100))

'''
#naive method
def primes_method1(n):
    out = list()
    for num in range(1, n+1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return out

'''