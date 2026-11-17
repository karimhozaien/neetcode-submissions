from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_map = defaultdict(list)
        sequences = 0
        my_list = sorted(nums)
        mmax = 0
        for i in range(len(nums)):
            if i == 0:
                my_map[sequences] = [my_list[i]]
            else:
                if my_list[i]-1 in my_map[sequences]:
                    my_map[sequences].append(my_list[i])
                else:
                    sequences += 1
                    my_map[sequences].append(my_list[i])
        values = list(my_map.values())
        mmax = values[0]
        for i in range(len(values)-1):
            if len(values[i]) < len(values[i+1]):
                mmax = values[i+1]
        values = mmax
        values2 = []
        for i in range(len(values)):
            if values[i] not in values2:
                values2.append(values[i])
        return len(values2)