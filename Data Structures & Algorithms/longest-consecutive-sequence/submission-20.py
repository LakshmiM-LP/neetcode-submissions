class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        seen=set()
        result=[]
        if nums == []:
            return 0
        else:
            for i in range(0,len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
            a=sorted(seen)
            if len(a)==1:
                    return 1
            for i in range(0,len(a)-1):
                compliment=a[i+1]-a[i]
                if compliment==1:
                    count+=1
                else:
                    count=1
                result.append(count)

   
        return (max(result))
                    
