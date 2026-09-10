'''
def two_sum(arr,targ):
    lookp={}
    for n,x in enumerate(arr,1):
        try:
            return lookp[x],n-1
        except KeyError:
            lookp.setdefault((targ-x),n-1)

a = (-3,4,3,90)
t = 0
print(two_sum(a,t))  
'''
'''
def fizzBuzz(n):
    i=1
    while i <=n:
        if i % 3 == 0 and i %5 == 0 :
            print ('FizzBuzz')
        elif i%3 ==0 and i%5 != 0 :
            print ('Fizz')
        elif i%3 !=0 and i%5 == 0 :
            print ('Buzz')
        else :
            print(i)
        i+=1
        
if __name__ == '__main__':
    n=15
    fizzBuzz(n)
'''
import calendar
def ada(year):
    calmonth = calendar.monthcalendar(year,10)   
    secondweek1 = calmonth[0]
    secondweek2 = calmonth[1]
    secondweek3 = calmonth[2]
    print (secondweek1)
    print (secondweek2)
    if secondweek1[calendar.TUESDAY] :
        secondTuesday = secondweek2[calendar.TUESDAY]
    else:
        secondTuesday = secondweek3[calendar.TUESDAY]
    print (secondTuesday)
    
if __name__ == '__main__':
    year=2017
    ada(year)
        
     