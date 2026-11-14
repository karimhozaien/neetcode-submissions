class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1
        res = []
        for i in range(len(numbers)):
            
            if numbers[index1] + numbers[index2] == target:
                res.append(index1+1)
                res.append(index2+1)
                return res

            if numbers[index1] + numbers[index2] > target:
                index2 -= 1

            if numbers[index1] + numbers[index2] < target:
                index1 += 1
                

                

        