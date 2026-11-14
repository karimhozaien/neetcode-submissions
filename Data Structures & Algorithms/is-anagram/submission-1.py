from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = defaultdict(list)
        s = list(s)
        t = list(t)
        t.sort()
        s.sort()
        if s == t:
            return True
        else:
            return False