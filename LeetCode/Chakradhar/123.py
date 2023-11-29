class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(idx, holding, rem):
            if idx >= len(prices):
                return 0

            key = (idx, holding, rem)
            if key in dp:
                return dp[key]

            if holding:
                dp[key] = max(
                    prices[idx] + dfs(idx+1, False, rem),
                    dfs(idx+1, True, rem)
                )
            else:
                if rem > 0:
                    dp[key] = max(
                        dfs(idx+1, True, rem-1) - prices[idx],
                        dfs(idx+1, False, rem)
                    )
                else:
                    dp[key] = 0

            return dp[key]

        dp = {}
        return dfs(0, False, 2)
