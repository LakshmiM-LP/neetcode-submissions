class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        result_left=[]
        result_right=[]
        left_product=1
        right_product=1
        for i in range(len(nums)):
            
            result_left.append(left_product)
            left_product*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            
            result_right.append(right_product)
            right_product*=nums[j]
        result_right=result_right[::-1]
        for i in range(len(nums)):
              answer.append(result_right[i]*result_left[i])
        return answer

        