class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fill(image,sr,sc,image[sr][sc],newColor)
        return image
    
    def fill(self,image,i,j,color,newColor):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[i]) or image[i][j] != color:
            return
        image[i][j] = newColor
        self.fill(image,i+1,j,color,newColor)
        self.fill(image,i-1,j,color,newColor)
        self.fill(image,i,j+1,color,newColor)
        self.fill(image,i,j-1,color,newColor)
        
