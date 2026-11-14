class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mm = {}
        nums = sorted(set(nums))
        n = len(nums)
        for i in range(n):
            if (nums[i] - 1) not in mm:
                mm[nums[i]] = [nums[i]]
            if  (nums[i] - 1) in mm:
                mm[nums[i]] = list(mm.get(nums[i]-1)) + [nums[i]]
        print(mm.items())
        lcs = max(mm.values() , key=len)
        lcs = len(lcs)
        return lcs
        