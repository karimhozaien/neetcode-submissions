from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        sorted_strs = sorted(strs)
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            map[sorted_word].append(strs[i])
        return map.values()


        