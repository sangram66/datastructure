# Python3 implementation to
# Divide two integers
# without using multiplication,
# division and mod operator
 
# Function to divide a by
# b and return floor value it
def divide(dividend, divisor):
     
    # Calculate sign of divisor
    # i.e., sign will be negative
    # either one of them is negative
    # only iff otherwise it will be
    # positive
     
    sign = (-1 if((dividend < 0) ^ (divisor < 0)) else 1);
     
    # remove sign of operands
    dividend = abs(dividend);
    divisor = abs(divisor);
     
    # Initialize
    # the quotient
    quotient = 0;
    temp = 0;
     
    # test down from the highest
    # bit and accumulate the
    # tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i;
            quotient |= 1 << i;
     
    return sign * quotient;
 
# Driver code
a = 10;
b = 3;
print(divide(a, b));
 
a = 43;
b = -8;
print(divide(a, b));
