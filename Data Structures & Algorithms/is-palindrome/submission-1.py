class Solution:
    def isPalindrome(self, s: str) -> bool:
        numStr=""

        for ch in s:
            if ch.isalnum():
                numStr+=ch.lower()
        if numStr==numStr[::-1]:
            return True
        return False
        
       

            
        
    

                


        