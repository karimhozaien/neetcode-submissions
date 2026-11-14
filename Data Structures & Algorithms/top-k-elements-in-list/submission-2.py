class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            if nums[i] in myMap:
                myMap[nums[i]] += 1
            else:
                myMap[nums[i]] = 1
                
        values_map = list(myMap.items())
        values = [list(item) for item in values_map]
        print(values)
        stack = [[''] for nums in nums]
        print(stack)
        for n,c in values:
             stack[c-1].append(n)
             if '' in stack[c-1]:
                stack[c-1].remove('')

        stack = stack[::-1]
        print(stack)
        res = []

        for i in range(len(stack)):
            if len(res) == k:
                return res
            if stack[i] != ['']:
                for j in range(len(stack[i])):
                    res.append(stack[i][j])
        return res
            

        



        




        
        