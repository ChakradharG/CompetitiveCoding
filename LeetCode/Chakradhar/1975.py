class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans, c, mn = 0, 0, abs(matrix[0][0])
        for row in matrix:
            for num in row:
                mn = min(mn, abs(num))
                if num < 0:
                    c += 1
                    ans -= num
                else:
                    ans += num

        if c % 2 == 0:
            return ans
        else:
            return ans - (2 * mn)
