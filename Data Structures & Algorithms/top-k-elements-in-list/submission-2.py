class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        a=sorted(freq.items(),key=lambda x:x[1])
        return[pair[0] for pair in a[-k:]]