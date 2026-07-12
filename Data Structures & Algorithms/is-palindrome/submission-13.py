class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.alphanum(s[l]):
                l+=1
            while r>l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        return True
    def alphanum(self,ch):
        return(ord("A")<=ord(ch)<=ord("Z")or
               ord("a")<=ord(ch)<=ord("z")or
               ord("0")<=ord(ch)<=ord("9"))

# | Code                                    | Purpose                                            |
# | --------------------------------------- | -------------------------------------------------- |
# | `while not self.alphanum(s[l]): l += 1` | Skip spaces, punctuation, etc.                     |
# | `while not self.alphanum(s[r]): r -= 1` | Skip spaces, punctuation, etc.                     |
# | `l += 1` and `r -= 1` after comparison  | Move to the **next pair of characters** to compare |

#this is an optimal solution 
# Here it is that we have to ignore if the element is not alphanum ,only consider alphanum
#here time complexity is  O(n), and space complexityis O(1)


        