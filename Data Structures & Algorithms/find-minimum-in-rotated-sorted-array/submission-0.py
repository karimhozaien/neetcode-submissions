class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0, len(nums) -1
        nums.sort()

        return nums[0]
        

        