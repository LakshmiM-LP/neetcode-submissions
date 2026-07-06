class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        left_product=1
        right_product=1
        for i in range(len(nums)):
            result.append(left_product)
            left_product*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            result[j]*=right_product
            right_product*=nums[j]
        return result

       
        
    