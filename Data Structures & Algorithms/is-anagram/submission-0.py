from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = defaultdict(list)
    
        for letters in s:
            anagram_map[s].append(letters)
            anagram_map[s].sort()
        for letters in t:
            anagram_map[t].append(letters)
            anagram_map[t].sort()
        if anagram_map[t] == anagram_map[s]:
            return True
        else:
            return False