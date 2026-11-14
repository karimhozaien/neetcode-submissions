class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) -1

        for i in range(len(matrix)):

            if matrix[i][right] < target:
                continue
            else:
                row = matrix[i]
                
                for i in range(len(row)):

                    print(row[right])
                    print(row[left])
                    midpoint = left + ((right - left) // 2)
                    print(midpoint)

                    if target == row[midpoint]:
                        return True
                    if target > row[midpoint]:
                        left = midpoint + 1
                    if target < row[midpoint]:
                        right = midpoint -1
                    
        return False
