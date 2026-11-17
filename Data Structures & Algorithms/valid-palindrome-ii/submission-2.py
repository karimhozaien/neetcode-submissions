class Solution:
    def validPalindrome(self, s: str) -> bool:
        error = 0 
        l,r = -1, len(s)
        for i in range(len(s)):
            l += 1
            r -= 1
            if l < r:
                print(l)
                print(r)
                if s[l] == s[r]:
                    continue
                else:
                    error += 1
        if l == r:
            error += 1
        if error > 1:
            return False
        else:
            return True

        