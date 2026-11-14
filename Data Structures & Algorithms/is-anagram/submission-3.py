class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ms[s[i]] = 1 + ms.get(s[i],0)
            mt[t[i]] = 1 + mt.get(t[i],0)
        if mt == ms:
            return True
        else:
            return False

