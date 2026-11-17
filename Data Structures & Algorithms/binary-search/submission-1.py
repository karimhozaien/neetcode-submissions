class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)
        mid = 0

        for i in range(len(nums)):
            mid = (r - l) // 2
            if target > nums[mid]:
                l = mid
            else:
                r = mid
            if target == nums[mid]:
                return mid
        return -1
        