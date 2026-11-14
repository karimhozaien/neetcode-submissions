class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mm = {}
        n = len(nums)
        res = []
        for i in range(n):
            mm[nums[i]] = 1 + mm.get(nums[i], 0)
        
        res = sorted(mm, key=mm.get, reverse=True)[:k]
        return res