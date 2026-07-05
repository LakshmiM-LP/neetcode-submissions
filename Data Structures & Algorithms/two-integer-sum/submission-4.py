class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={} #dictionary
        for i in range(len(nums)):
            compliment=target - nums[i]
            if compliment in result:
                return [result[compliment],i]
            
            result[nums[i]] =i





        