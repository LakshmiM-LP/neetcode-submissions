class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_left=0
        max_right=0
        max_water=0
        while l < r:
            max_left=max(max_left,height[l])
            max_right=max(max_right,height[r])
            if max_left>max_right:
                water=abs(max_right-height[r])
                max_water+=water
                r-=1
            else:
                water=abs(max_left-height[l])
                max_water+=water
                l+=1
        return max_water


        
        