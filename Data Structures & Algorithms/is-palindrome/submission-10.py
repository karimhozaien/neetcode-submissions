class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        strs = []
        for i in range(n):
            if s[i].isalnum():
                strs.append(s[i])
        l,r = 0, len(strs)-1
        while l < r:
            print(strs[l],strs[r])
            if strs[l] == strs[r]:
                l += 1
                r -= 1
            else:
                return False
        return True



