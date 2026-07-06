class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        a= sorted(freq.items(),key=lambda x:x[1])
        return [pair[0] for pair in a[-k:]]

