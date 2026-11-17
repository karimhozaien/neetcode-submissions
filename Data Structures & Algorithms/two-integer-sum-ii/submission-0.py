class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        index1 = 0
        index2 = len(nums)-1
        res = []
        for i in range(len(nums)):
            if nums[index1] + nums[index2] == target:
                res.append(index1+1)
                res.append(index2+1)
                return res
            elif nums[index1] + nums[index2] > target:
                index2 -=1
            elif nums[index1] + nums[index2] < target:
                index1 =+1
                

                

        