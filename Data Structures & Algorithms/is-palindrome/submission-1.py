class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()

        

        while right >= left:
            if s[left].isalpha() == False:
                left+=1
            if s[right].isalpha() == False:
                right-=1
            if s[right] == s[left]:
                print(s[left])
                print(s[right])
                right-=1
                left+=1
            else:
                return False
            
        return True


        