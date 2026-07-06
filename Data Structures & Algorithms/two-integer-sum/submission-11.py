class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                compliment=nums[i]+nums[j]
                if compliment==target:
                    return[i,j]
    #this solution is correct but not optimalo because of its complexity is n square
        