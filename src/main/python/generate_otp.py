import math
import random
def gen_otp():
    lent=6
    otp=""
    strin="1256372615873252492rxgjdxhvdhfvxkdfsvdkfhgwi3yrftq82y397bt2r1o72n31%!$^$&^%*$#$%&^*(*^*$%@#@#%&^*&^"
    for i in range(lent):
        otp+=strin[int(math.floor(random.random() * len(strin)))]
    
    return (otp)
if __name__ == "__main__" :
    print("OTP of length 6:", gen_otp())