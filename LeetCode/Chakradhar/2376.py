class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        def dfs(i, tight, mask, nz):
            if i == len(num):
                return int(nz)
            key = (i, tight, mask, nz)
            if key not in memo:
                r = int(num[i]) if tight else 9
                res = 0
                for d in range(r+1):
                    bm = 0b1<<d
                    if mask&bm:
                        continue
                    if d == 0:
                        if nz:
                            res += dfs(i+1, tight and d==int(num[i]), mask|bm, nz)
                        else:
                            res += dfs(i+1, tight and d==int(num[i]), mask, nz)
                    else:    
                        res += dfs(i+1, tight and d==int(num[i]), mask|bm, True)
                memo[key] = res
            return memo[key]

        memo = {}
        num = str(n)
        return dfs(0, True, 0, False)
