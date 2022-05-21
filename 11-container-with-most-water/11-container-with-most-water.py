class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        r , l = len(height) - 1 , 0
        max_area = 0
        
        while l < r:
            max_height = min(height[l], height[r])
            area = max_height * (r-l)
            
            max_area = max(max_area, area)
            
            if height[l] > height[r]:r-=1
            else: l+=1
            
        return max_area