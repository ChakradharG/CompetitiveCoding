class Solution:
    def knightDialer(self, n: int) -> int:
        def neighbors(num):
            if num == 0:
                return [4, 4]
            elif num == 1:
                return [4, 2]
            elif num == 2:
                return [3, 1]
            elif num == 3:
                return [4, 2]
            elif num == 4:
                return [0, 3, 1]
            # elif num == 5:
            #     return []
            # elif num == 6:
            #     return [0, 1, 7]
            # elif num == 7:
            #     return [2, 6]
            # elif num == 8:
            #     return [1, 3]
            # elif num == 9:
            #     return [2, 4]

        def dfs(idx, num):
            key = (idx, num)
            if key in dp:
                return dp[key]

            if idx == n-1:
                dp[key] = 1
                return 1

            dp[key] = 0
            for neighbor in neighbors(num):
                dp[key] += dfs(idx+1, neighbor)

            return dp[key]

        dp = {}
        cnt, mod = 0, 10**9 + 7
        for i in range(1, 5):
            dfs(0, i)
            cnt = (cnt + dp[(0, i)]) % mod
        dfs(0, 0)
        cnt = (2 * cnt + dp[(0, 0)]) % mod

        if n == 1:
            cnt += 1    # for 5
        return cnt
