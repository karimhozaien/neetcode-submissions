from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = defaultdict(list) 
        diff = 0
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sum_map.keys():
                return [sum_map.get(diff)[0],i]
            sum_map[nums[i]].append(i)
        return False

            
