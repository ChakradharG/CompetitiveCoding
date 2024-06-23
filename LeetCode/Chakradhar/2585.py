class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        def dfs(i, cur):
            if cur == target:
                return 1
            elif cur > target:
                return 0
            if i == len(types):
                return 0

            key = (i, cur)
            if key not in memo:
                memo[key] = 0
                for cnt in range(types[i][0]+1):
                    memo[key] = (
                        memo[key] + 
                        dfs(i+1, cur + cnt*types[i][1])
                    ) % MOD

            return memo[key]

        memo = {}
        MOD = 10**9 + 7
        return dfs(0, 0)
