from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = defaultdict(list)

        for n in nums:
            duplicate_map[n].append(n)
            iterations = duplicate_map.values()
            print(iterations)
            if len(duplicate_map[n]) > 1:
                return True
        return False
            

