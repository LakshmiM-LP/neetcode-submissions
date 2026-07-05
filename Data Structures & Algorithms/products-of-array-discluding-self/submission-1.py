class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product=1
        right_product =1
        answer=[]
        for i in range(len(nums)):
            answer.append(left_product)
            left_product*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            answer[j] *= right_product
            right_product*=nums[j]
        return answer


        