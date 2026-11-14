class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mymap = {}
        for i in range(len(nums)):
            if nums[i] not in mymap:
                mymap[nums[i]] = 1
            else:
                return True
        return False