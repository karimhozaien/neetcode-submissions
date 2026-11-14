class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1
        mid = l + ((r-l)//2)
        pivot = -1
        change = False
        if len(nums) > 1:
            if nums[l] < nums[mid]:
                for i in range(mid,r):
                    if nums[i] > nums[i+1]:
                        pivot = nums[i+1]
                        return pivot
            else:
                for i in range(l,mid+1):
                    if nums[i] > nums[i+1]:
                        pivot = nums[i+1]
                        return pivot
        if pivot == -1:
            return nums[0]
        

        