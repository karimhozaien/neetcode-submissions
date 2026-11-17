class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) -1

        for i in range(len(matrix)):

            if matrix[i][right] < target:
                continue
            else:
                row = matrix[i]
                if target in row:
                    return True 
                else:
                    return False
