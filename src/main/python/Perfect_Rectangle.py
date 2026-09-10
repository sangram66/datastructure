#391. Perfect Rectangle
#https://leetcode.com/problems/perfect-rectangle/

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        hs = set()
        area = 0
        for rec in rectangles:
            top_left = (rec[0], rec[1])
            top_right = (rec[0], rec[3])
            bottom_left = (rec[2], rec[1])
            bottom_right = (rec[2], rec[3])
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            for i in [top_left, top_right, bottom_left, bottom_right]:
                if i not in hs:
                    hs.add(i)
                else:
                    hs.remove(i)
                print (hs)
        if len(hs) != 4:
            return False
        hs = sorted(hs)
        print (hs)
        first = hs.pop(0)
        print (first)
        last = hs.pop()
        print (last)
        #print ((last[0] - first[0]) * (last[1] - first[1]))
        return area == (last[0] - first[0]) * (last[1] - first[1])

sol=Solution()
rectangles =[
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
print (sol.isRectangleCover(rectangles))
