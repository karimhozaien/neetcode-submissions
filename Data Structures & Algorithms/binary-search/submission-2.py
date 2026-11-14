class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)
        mid = 0

        for i in range(len(nums)):
            mid = l + (r - l)// 2
            print(l)
            print(r)
            print(mid)
            if target > nums[mid]:
                l = mid
            elif target < nums[mid]:
                r = mid
            if target == nums[mid]:
                return mid
            
        return -1
        