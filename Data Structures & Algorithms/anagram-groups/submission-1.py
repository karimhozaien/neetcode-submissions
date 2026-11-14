from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        string = ''
        for i in range(len(strs)):
            string = sorted(strs[i])
            string = ''.join(string)
            my_map[string].append(strs[i])
        my_list = list(my_map.values())
        return my_list
            


        