class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        max_water=0
        while l < r:
            width=r-l
            height=min(heights[l],heights[r])
            water= width * height
            max_water=max(max_water,water)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_water

            

#optimal solution
# width = 7 - 1 = 6
# water_height = min(7,6) = 6

# water = 6 × 6 = 36
# FORMULA
# water = width * min(height1, height2)