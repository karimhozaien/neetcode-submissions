from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        s = ''.join(s)
        t = ''.join(t)
        if s == t:
            return True
        else:
            return False