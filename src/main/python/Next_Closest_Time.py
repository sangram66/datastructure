#https://leetcode.com/explore/featured/card/google/67/sql-2/471/
class Solution(object):
    def nextClosestTime(self, time):
        hour,minute=time.split(':')
        nums=sorted(set(hour+minute))
        two_digit_values=[a+b for a in nums for b in nums]
        
        i=two_digit_values.index(minute)
        if i+1 < len(two_digit_values) and two_digit_values[i+1] < "60":
            return hour + ':' + two_digit_values[i+1]
        
        i=two_digit_values.index(hour)
        if i+1 < len(two_digit_values) and two_digit_values[i+1] < "24":
            return two_digit_values[i+1] + ':' + two_digit_values[0]
        
        return two_digit_values[0]+':'+two_digit_values[0]
    
if __name__=='__main__':
    sol=Solution()
    print sol.nextClosestTime("19:39")
    

        