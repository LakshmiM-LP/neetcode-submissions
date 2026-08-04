class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for word in strs:
            sort=sorted(word)
            a="".join(sort)
            if a not in freq:
                freq[a]=[]
            freq[a].append(word)
        return list(freq.values())