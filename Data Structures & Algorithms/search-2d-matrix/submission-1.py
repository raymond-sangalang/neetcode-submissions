class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n  = len(matrix), len(matrix[0])    # length of the rows and columns
        t = m*n                                # total number of elements
        l, r = 0, t-1                          # left and right ends for search boundaries

        while l <= r:
            m = (l+r) // 2     # mid indice
            i = m // n         # row given by integer division
            j = m % n          # column given by the modulus

            # Check if the middle indice is the target value
            # or update the left or right bounds of the search
            # variables
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                r = m - 1
            else:
                l = m + 1
        
        return False

        # Time: O(log(m* n))
        # Space: O(1)