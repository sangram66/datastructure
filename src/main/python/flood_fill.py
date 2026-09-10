'''
https://leetcode.com/problems/flood-fill/
'''



class Solution(object):
    def floodfillUtil(self,image,sr,sc,prev,newColor):
        if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc]!= prev or image[sr][sc] == newColor):
            return
        image[sr][sc] = newColor 
        self.floodfillUtil(image,sr+1,sc,prev,newColor)
        self.floodfillUtil(image,sr-1,sc,prev,newColor)
        self.floodfillUtil(image,sr,sc+1,prev,newColor)
        self.floodfillUtil(image,sr,sc-1,prev,newColor)
        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        prev = image[sr][sc]
        self.floodfillUtil(image,sr,sc,prev,newColor)
        
        return (image)
    
    
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1 
sc = 1
newColor = 2


print (Solution().floodFill(image,sr,sc,newColor))


