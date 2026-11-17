class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1
        mid = l + ((r-l)//2)
        pivot = 0
        if nums[l] < nums[mid]:
            for i in range(r):
                if nums[i]+1 != nums[i+1]:
                    pivot = nums[i+1]
                    return pivot 
        else:
            for i in range(mid,r):
                if nums[i-1] != nums[i]-1:
                    pivot = nums[i]
                    return pivot

        

        