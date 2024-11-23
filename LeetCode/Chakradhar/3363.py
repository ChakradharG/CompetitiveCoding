class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0

        memo1 = {}
        def dfs1(i, j):
            if j == n-1:
                if i == n-1:
                    return 0
                else:
                    return -math.inf
            key = (i, j)
            if key not in memo1:
                memo1[key] = dfs1(i, j+1)
                if i < n-1:
                    memo1[key] = max(memo1[key], dfs1(i+1, j+1))
                if i > 0:
                    memo1[key] = max(memo1[key], dfs1(i-1, j+1))
                memo1[key] += fruits[i][j]
            return memo1[key]

        memo2 = {}
        def dfs2(i, j):
            if i == n-1:
                if j == n-1:
                    return 0
                else:
                    return -math.inf
            key = (i, j)
            if key not in memo2:
                memo2[key] = dfs2(i+1, j)
                if j < n-1:
                    memo2[key] = max(memo2[key], dfs2(i+1, j+1))
                if j > 0:
                    memo2[key] = max(memo2[key], dfs2(i+1, j-1))
                memo2[key] += fruits[i][j]
            return memo2[key]

        ans += dfs1(n-1, 0) + dfs2(0, n-1)
        return ans