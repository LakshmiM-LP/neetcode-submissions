class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        seen=set()
        result=[]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l < r:
                curr_sum= nums[i]+nums[l]+nums[r]
                if curr_sum==0:
                    triplet= (nums[i],nums[l],nums[r])
                    l,r=l+1,r-1
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append(triplet)
                elif curr_sum>0:
                    r-=1
                else:
                    l+=1
        return result