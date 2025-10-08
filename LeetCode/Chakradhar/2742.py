class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        def dfs(i, done):
            if done >= n:
                return 0
            if i == n:
                return math.inf

            key = (i, done)
            if key not in memo:
                res = min(
                    dfs(i+1, done),  # skip
                    cost[i] + dfs(i+1, done+time[i]+1)
                )
                memo[key] = res
            return memo[key]

        memo = {}
        n = len(cost)
        return dfs(0, 0)
