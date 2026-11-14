class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index1 = 0
        index2 = len(nums) -1

        for i in range(len(nums)):
            midpoint = index1 + int(index2 - index1)//2
            
            midpointV = nums[midpoint]
            print(midpointV)
            print(midpoint)
            if target == midpointV:
                return midpoint

            if target > midpointV:
                index1 = midpoint +1
            else:
                index2 = midpoint -1
        return -1
        