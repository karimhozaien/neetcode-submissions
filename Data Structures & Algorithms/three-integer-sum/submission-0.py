from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            copy = nums.copy()
            target = nums[i]
            copy.remove(target)
            l = 0
            r = len(copy)-1

            for j in range(len(copy)):
                if l >= r:
                    break
                if (copy[l] + copy[r] + target) == 0: 
                    answer = [target,copy[l],copy[r]]
                    answer.sort()
                    if answer not in res:
                        print(target)
                        print(copy)
                        print(l)
                        print(r)
                        print('passed')
                        print('result ' + str(answer))
                        res.append([target,copy[l],copy[r]])
                    l += 1
                elif copy[l] + copy[r] + target < 0:
                    l += 1
                elif copy[l] + copy[r] + target > 0:
                    r -= 1
        return res






