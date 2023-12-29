class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        def dfs(cur, i, d):
            if i == n:
                if d == 0:
                    return 0
                return math.inf
            if d == 0:
                return math.inf

            cur = max(cur, jobDifficulty[i])
            key = (cur, i, d)
            if key not in memo:
                memo[key] = min(
                    cur + dfs(0, i+1, d-1),
                    dfs(cur, i+1, d) 
                )

            return memo[key]

        memo = {}
        return dfs(0, 0, d)
