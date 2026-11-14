from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_map = {}
        mult = 0
        for i in range(len(nums)):
            nums2 = nums.copy()
            print(nums2)
            nums2.remove(nums[i])
            print(nums2)
            mult = reduce(lambda x, y: x*y,nums2)
            my_map[i] = mult
        my_list = list(my_map.values())
        return my_list