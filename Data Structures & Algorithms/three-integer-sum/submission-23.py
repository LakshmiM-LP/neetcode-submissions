class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                continue
            while l <r:
                curr_sum=nums[i]+nums[l]+nums[r]
                if curr_sum==0:
                    result.append([nums[i],nums[l],nums[r]])
                    l,r=l+1,r-1
                    while l <r and nums[l-1]==nums[l]:
                        l+=1
                    while l<r and nums[r+1]==nums[r]:
                        r-=1
                elif curr_sum>0:
                    r-=1
                else:
                    l+=1
        return result
