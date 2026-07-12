class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        higher_l=0
        higher_r=0
        water=0
        while l<r:
            higher_l=max(higher_l,height[l])
            higher_r=max(higher_r,height[r])
            if higher_r<higher_l:
                water+=higher_r-height[r]
                r-=1
            else:
                water+=higher_l-height[l]
                l+=1
        return water

        