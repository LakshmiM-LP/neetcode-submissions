class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=0
        max_right=0
        water=0
        l,r=0,len(height)-1
        while l < r:
            max_left=max(max_left,height[l])
            max_right=max(max_right,height[r])
            if max_left<=max_right:
                water+=max_left-height[l]
                l+=1
            else:
                water+=max_right-height[r]
                r-=1
        return water


        