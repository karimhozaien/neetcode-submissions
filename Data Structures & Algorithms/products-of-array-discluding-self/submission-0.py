from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_map = {}
        mult = 0
        for i in range(len(nums)):
            nums2 = nums.copy()
            nums2.remove(nums[i])
            mult = reduce(lambda x, y: x*y,nums2)
            my_map[nums[i]] = mult
        my_list = list(my_map.values())
        return my_list