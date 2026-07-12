class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for words in strs:
            sort_words=sorted(words)
            a="".join(sort_words)
            if a not in freq:
                freq[a]=[]
            freq[a].append(words)
        return list(freq.values())

        
        