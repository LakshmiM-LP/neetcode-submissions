class Solution:
    def isPalindrome(self, s: str) -> bool:
        numstr=""
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            else:
                numstr+=s[i]
        if numstr.lower()==numstr.lower()[::-1]:
            return True
        else:
            return False

            
            

        
           
        



        