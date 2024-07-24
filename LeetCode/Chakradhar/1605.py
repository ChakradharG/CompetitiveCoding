class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ans = [[0 for j in range(n)] for i in range(m)]

        i, j = 0, 0
        while (i < m) and (j < n):
            if rowSum[i] <= colSum[j]:
                ans[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                rowSum[i] = 0
                i += 1
            else:
                ans[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                colSum[j] = 0
                j += 1

        return ans
