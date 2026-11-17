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
        freq = values.reverse()

        res = []

        for n,c in values:
            if len(res) == k:
                return res
            if str(n).isalnum():
                res.append(n)
        return res


        




        
        