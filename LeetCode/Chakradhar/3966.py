class Solution:
    def digitDP(self, num):
        @cache
        def dfs(i, tight, prev, started):
            if i == n:
                return 1
            res = 0
            if started:
                l = max(0, prev - self.k)
                r = min(num[i] if tight else 9, prev + self.k)
            else:
                l = 0
                r = num[i] if tight else 9
            for d in range(l, r+1):
                res += dfs(i+1, tight and (d==num[i]), d, started or d>0)
            return res
        num = list(map(int, str(num)))
        n = len(num)
        return dfs(0, True, 0, False)

    def goodIntegers(self, l: int, r: int, k: int) -> int:
        self.k = k
        return self.digitDP(r) - self.digitDP(l-1)
