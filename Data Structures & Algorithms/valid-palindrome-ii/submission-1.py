class Solution:
    def validPalindrome(self, s: str) -> bool:
        error = 0 
        l,r = 0, len(s)-1
        for i in range(len(s)):
            if l < r:
                print(s[l])
                print(s[r])
                if s[l] == s[r]:
                    continue
                else:
                    error += 1
                l += 1
                r -= 1
        if l == r:
            error += 1
        if error > 1:
            return False
        else:
            return True

        