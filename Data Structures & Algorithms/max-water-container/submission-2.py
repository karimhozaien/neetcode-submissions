class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        max_height = 0
        index1 = 0
        index2 = len(heights)-1

        while index1 < index2:

            value = (index2 - index1) * min(heights[index1], heights[index2])
            if heights[index1] < heights[index2]:
                index1 += 1
            else:
                index2 -= 1
            
            if value > max_height:
                max_height = value
        
        return max_height
        