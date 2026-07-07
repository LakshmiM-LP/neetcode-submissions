class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=[]
        temp=s.lower()
        for ch in temp:
            if ch.isalnum():
                result.append(ch)
            else:
                continue
        if result==result[::-1]:
            return True
        return False
