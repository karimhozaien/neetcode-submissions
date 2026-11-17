class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while right >= left:
            if s[left].isalpha() == False:
                left+=1
            if s[right].isalpha() == False:
                right-=1
            if s[right].lower() == s[left].lower():
                right-=1
                left+=1
            else:
                return False
            
        return True


        