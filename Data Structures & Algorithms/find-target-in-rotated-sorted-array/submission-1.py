class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums) -1
        mid = l + ((r-l)//2)
        pivot = -1
        pivot_loc = -1
        if len(nums) > 1:
            if nums[l] < nums[mid]:
                for i in range(mid,r):
                    if nums[i] > nums[i+1]:
                        pivot = nums[i+1]
                        pivot_loc = i+1
            else:
                for i in range(l,mid+1):
                    if nums[i] > nums[i+1]:
                        pivot = nums[i+1]
                        pivot_loc = i+1
        if pivot == -1:
            pivot = nums[0]
            pivot_loc = 0
        
        if target not in nums:
            return -1
        if nums[l] < target < nums[pivot_loc-1]:
            for i in range(l,pivot_loc):
                if target == nums[i]:
                    return i
        else:
            for i in range(pivot_loc,r):
                if target == nums[i]:
                    return i