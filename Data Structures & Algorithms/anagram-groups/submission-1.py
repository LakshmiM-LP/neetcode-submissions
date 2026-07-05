class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        freq={}
        for words in strs:
            sort_words=sorted(words)
            a="".join(sort_words)
            if a not in freq:
                freq[a]=[]
            freq[a].append(words)
        return list(freq.values())
            

            
           
            

#result is the original list where we can append original words
#Key = sorted version of the word.
#Value = list of original words.