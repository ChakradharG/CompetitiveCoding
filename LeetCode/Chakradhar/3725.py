class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def dfs(i, cur):
            if i == m:
                return cur == 1
            key = (i, cur)
            if key not in memo:
                res = 0
                for j in range(n):
                    ncur = gcd(cur, mat[i][j])
                    if ncur == 1:
                        x = (n ** (m - i - 1)) % MOD
                    else:
                        x = dfs(i+1, ncur)
                    res = (res + x) % MOD
                memo[key] = res
            return memo[key]

        m, n = len(mat), len(mat[0])
        memo = {}
        MOD = 10**9 + 7
        ans = 0
        for j in range(n):
            ans = (ans + dfs(1, mat[0][j])) % MOD
        return ans
