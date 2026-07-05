class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result=[]
        repeat=[]
        for i in range(len(nums)):
            if nums[i] not in result:
                result.append(nums[i])
            else:
                repeat.append(nums[i])
        if len(repeat)>0:
            return True
        else:
            return False
