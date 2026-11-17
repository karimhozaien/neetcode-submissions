class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        max_height = 0
        index1 = 0
        index2 = len(heights)-1

        for ind in range(len(heights)):

            value = (index2 - index1) * min(heights[index1], heights[index2])

            if heights[index1] < heights[index2]:
                index1 += 1
                print("index 1+")
            if heights[index1] > heights[index2]:
                index2 -= 1
                print("index 2-")
            
            if value > max_height:
                max_height = value
        
        return max_height
        