from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = defaultdict(list)
        for i in range(len(nums)):
            my_dict[nums[i]].append(1)
        if len(my_dict.keys()) < len(nums):
            return True
        return False