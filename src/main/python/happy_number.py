#https://leetcode.com/explore/interview/card/apple/348/others/3143/

def isHappy( n):

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            print (n,digit)
            total_sum += digit ** 2
        print (total_sum)
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        print (seen)
        seen.add(n)
        n = get_next(n)

    return n == 1
print (isHappy(3))
        