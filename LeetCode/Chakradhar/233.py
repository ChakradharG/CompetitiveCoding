class Solution:
    def countDigitOne(self, n: int) -> int:
        def dfs(i, tight, ones):
            if i == n:
                return ones
            key = (i, tight, ones)
            if key not in memo:
                if tight:
                    if num[i] == '0':
                        memo[key] = dfs(i+1, True, ones)    # can only place 0
                    elif num[i] == '1':
                        memo[key] = (
                            dfs(i+1, False, ones) + # place 0
                            dfs(i+1, True, ones+1)  # place 1
                        )
                    else:
                        memo[key] = (
                            (int(num[i])-1) * dfs(i+1, False, ones) +   # place all digits < num[i] (except 1)
                            dfs(i+1, False, ones+1) +                   # place 1
                            dfs(i+1, True, ones)                        # place num[i]
                        )
                else:
                    memo[key] = (
                        9 * dfs(i+1, False, ones) + # place all digits (except 1)
                        dfs(i+1, False, ones+1)     # place 1
                    )
            return memo[key]

        memo = {}
        num = str(n)
        n = len(num)
        return dfs(0, True, 0)
