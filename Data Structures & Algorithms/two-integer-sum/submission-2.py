class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mm = {}
        n = len(nums)
        res = []
        for i in range(n):
            print(mm.items())
            diff = target - nums[i] 
            print(diff)
            if diff in mm:
                print('yes')
                res.append(mm[diff])
                res.append(i)
                return res
            else:
                mm[nums[i]] = i
        