from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))  # Remove duplicates and sort the list
        myMap = {}
        current_list = []
        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i-1]+1:
                current_list.append(nums[i])
            else:
                myMap[len(myMap)] = current_list
                current_list = [nums[i]]
        myMap[len(myMap)] = current_list

        longest_seq = max(len(sequence) for sequence in myMap.values())
        return longest_seq