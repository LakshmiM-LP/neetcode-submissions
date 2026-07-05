class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        count=1
        result=[]
        if nums==[]:
            return 0
        else:
            for num in nums:
                if num not in seen:
                    seen.add(num)
            seen=sorted(seen)
            if len(seen)==1:
                return 1
            for i in range(0,len(seen)-1):
                compliment=seen[i+1]-seen[i]
                if compliment==1:
                    count+=1
                else:
                    count=1
                result.append(count)
        return max(result)
        
        