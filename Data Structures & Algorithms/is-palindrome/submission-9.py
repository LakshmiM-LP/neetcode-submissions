class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l < r:
            while l<r and not self.alnum(s[l]):
                l+=1
            while r>l and not self.alnum(s[r]):
                r-=1
            while s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        return True   
                
    def alnum(self,ch):
        return(ord("A")<=ord(ch)<=ord("Z")or
               ord("0")<=ord(ch)<=ord("9")or
               ord("a")<=ord(ch)<=ord("z"))


            



            
            

        
           
        



        