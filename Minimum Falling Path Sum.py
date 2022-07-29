#TC :O(n^2)
#SC :O(1)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
                if col == 0:
                    matrix[row][col] = min(matrix[row-1][col]+matrix[row][col],matrix[row-1][col+1]+matrix[row][col])
                elif col == len(matrix)-1:
                    matrix[row][col] = min(matrix[row-1][col]+matrix[row][col],matrix[row-1][col-1]+matrix[row][col])
                else:
                    matrix[row][col] = min(matrix[row-1][col]+matrix[row][col],matrix[row-1][col-1]+matrix[row][col],
                                          matrix[row-1][col+1]+matrix[row][col])
        
        
        return min(matrix[-1])
                    