''''
class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        interv=[]
        for i in range(len(intervals)):
            interv.append([intervals[i].start,intervals[i].end])
        interv.sort()
        print ("sorted interval :"+str(interv))
        res=[]
        while(len(interv)>0):
            if len(interv)==1:
                print ("inside 1st if")
                print (interv[0])
                res.append(interv[0])
                interv.pop(0)
                continue
            if interv[0][1]>=interv[1][0]:
                print ("inside 2nd if")
                print (interv[0][1],interv[1][0])
                tmp=[interv[0][0],max(interv[0][1],interv[1][1])]
                print ("tmp :"+str(tmp))
                interv[0]=tmp
                print ("interv :"+str(interv))
                x=interv.pop(1)
                print ("pop :"+str(x))
                continue
            print ("res0  "+str(res))
            res.append(interv[0])
            print ("res  "+str(res))
            interv.pop(0)
        return res

if __name__=='__main__':
    #inter=Interval()
    i1=Interval(1,3)
    i2=Interval(2,6)
    i3=Interval(8,10)
    i4=Interval(15,18)
    intervals= [i1,i2,i3,i4]
    opt=Solution().merge(intervals)
    print (opt)
    
'''


class Solution(object):
    def merge(self,ll):
        ll.sort()
        print (ll)
        l=len(ll)
        i=1
        while i<l:
            if ll[i-1][1]>=ll[i][0]:
                ll[i-1][1]=max(ll[i-1][1],ll[i][1])
                ll.pop(i)
                l=l-1
            else:
                i=i+1
        return ll
intervals= [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))

