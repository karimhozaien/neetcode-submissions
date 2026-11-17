import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        mm = {}
        for i in range(n):
            if nums[i] == 0:
                copy = nums.copy()
                copy.remove(0)
                prod = math.prod(copy)
            else :
                if math.prod(nums) == 0:
                    prod = 0
                else:
                    prod = math.prod(nums) / nums[i]
            res.append(int(prod))
            print(res)
        return res

        