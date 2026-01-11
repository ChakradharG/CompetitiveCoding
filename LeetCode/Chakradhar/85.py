class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
        matrix[0].append(0)
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    matrix[i][j] = matrix[i-1][j] + 1
                else:
                    matrix[i][j] = 0
            matrix[i].append(0)

        ans = 0
        for i in range(m):
            stack = []
            for j in range(n+1):
                prev = j
                while stack and matrix[i][j] < stack[-1][0]:
                    x, k = stack.pop()
                    ans = max(ans, x * (j - k))
                    prev = k
                stack.append((matrix[i][j], prev))

        return ans

