class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        seen =set()
        answ=0
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
            answ=max(answ,len(seen))
        return answ
        