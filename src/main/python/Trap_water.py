#HARD # https://leetcode.com/problems/trapping-rain-water/ 
"""
class Solution(object):
    def trap(self, height):
        
        s = []
        tS = 0 #Total Sum
        cS = 0 #Current Sum
        for i, h in enumerate(height):
            if len(s) == 0 and h==0: continue
            if len(s) == 0 and h!=0:
                s.append((i,h))
            elif s[-1][1] > h:
                s.append((i,h))
            else: 
                while len(s)!=0 and s[-1][1] <= h:
                    val = s.pop()

                    if len(s)!=0: 
                        tS += (i-s[-1][0]-1)*(min(s[-1][1], h) - val[1])
                
                        
                s.append((i,h))
                
        return tS

if __name__=='__main__':
    sol=Solution()    
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    res=sol.trap(height)
    print (res)
"""
"""
def trap(heights):
    if not heights or len(heights) < 3:
        return 0

    size = len(heights)
    lBound = [0] * size
    rBound = [0] * size

    h = heights[0]
    print ("h:"+str(h))
    for i in range(size):
        lBound[i] = h = max(h, heights[i])
    print (lBound)
    print ("--------------")
    h = heights[size - 1]
    print ("h:"+str(h))
    for i in reversed(range(size)):
        rBound[i] = h = max(h, heights[i])
    print (rBound)
    water = 0
    for i in range(size):
        water += min(lBound[i], rBound[i]) - heights[i]

    return water

height=[0,1,0,2,1,0,1,3,2,1,2,1]
print ("height:"+str(height))
res=trap(height)
print (res)
"""
'''
class Solution(object):
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights or len(heights) < 3:
            return 0

        level = water = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            # Take the lower side as the current ground level.
            print ('-------------------------------------------------')
            it = heights[i if heights[i] < heights[j] else j]
            print ('it: '+str(it))
            # Advance the lower side close to the higher side.
            print ("[i] , [j]:"+str(i)+'    ,   '+str(j))
            print ("heights[i] < heights[j]:"+str(heights[i])+'    ,   '+str(heights[j]))
            if heights[i] < heights[j]:
                i += 1
                print ('i: '+str(i))
                
            else:
                j -= 1
                print ('j: '+str(j))
            print ("level > it:"+str(level)+'    ,   ' +str(it))
            if level > it:
                # If the ground level is lower than the water level, fill it
                # with the water.
                water += level - it
                print ("water: "+str(water))
            else:
                # Update the water level.
                level = it
                print ("level: "+str(level))
        return water
if __name__=='__main__':
    sol=Solution()    
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    #height=[1,2,1,2,3,1,0,1,2,0,1,0]
    #height=[1,2]
    res=sol.trap(height)
    print (res)
    
'''
def trap_water(heights):
    maxes = [0 for i in heights]
    print (maxes)
    leftmax=0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i]=leftmax
        
        leftmax=max(leftmax,height)
    print ("leftmax: "+str(maxes))
    rightmax=0
    for i in reversed(range(len(heights))):
        print("i "+str(i))
        height = heights[i]
        print("height "+str(height))
        minheight = min(rightmax,maxes[i])
        print("minheight "+str(minheight))
        if height < minheight:
            maxes[i] = minheight - height
            print ("inside if, maxes "+str(maxes))
        else:
            maxes[i] = 0
            print ("inside else, maxes "+str(maxes))
        rightmax= max(rightmax,heights[i])
        print ("rightmax "+str(rightmax))
    return sum(maxes)

#height=[0,1,0,2,1,0,1,3,2,1,2,1]
#height=[1,8,6,2,5,4,8,3,7]
height=[1,2,1,2]
print (trap_water(height))