class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=[]
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                width=j-i
                height=min(heights[i],heights[j])
                water= width * height
                result.append(water)
        return max(result)

        