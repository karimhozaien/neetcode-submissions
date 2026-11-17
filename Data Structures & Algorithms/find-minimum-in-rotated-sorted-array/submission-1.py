class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1
        mid = l + ((r-l)//2)
        pivot = 0
        if nums[l] < nums[mid]:
            for i in range(mid,r):
                if nums[i+1] == nums[i]+1:
                    continue
                else:
                    pivot = nums[i+1]
        else:
            for i in range(mid+1):
                if nums[i+1] == nums[i]+1:
                    continue
                else:
                    pivot = nums[i+1]
        
        return pivot

        

        