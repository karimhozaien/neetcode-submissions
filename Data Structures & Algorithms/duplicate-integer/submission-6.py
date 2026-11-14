class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mm = {}
        for i in range(len(nums)):
            print(mm.values())
            if nums[i] in mm:
                return True
            mm[nums[i]] = 1 + mm.get(nums[i], 0)
            
        return False