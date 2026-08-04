class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        stoneValue.extend([0, 0])

        dp = [0] * (n + 3)
        for i in reversed(range(n)):
            dp[i] = max(
                stoneValue[i] - dp[i+1],
                stoneValue[i] + stoneValue[i+1] - dp[i+2],
                stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3],
            )

        if dp[0] < 0:
            return "Bob"
        elif dp[0] == 0:
            return "Tie"
        else:
            return "Alice"

