class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            stack.append(min(nums))
            nums.remove(min(nums))
        return stack

        