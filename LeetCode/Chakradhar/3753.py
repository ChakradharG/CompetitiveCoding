class Solution:
    def countWaviness(self, num: List[int]) -> int:
        @cache
        def dfs(i, tight, prv1, prv2, started):
            if i == n:
                return 1, 0 # ways, sum
            ws, sm = 0, 0
            r = num[i] if tight else 9
            for d in range(r+1):
                t = tight and (d == num[i])
                s = started or (prv1 != 0)
                cws, csm = dfs(i+1, t, prv2, d, s)
                ws += cws
                sm += csm
                if s and (prv1 < prv2 > d or prv1 > prv2 < d):
                    # if i-2, i-1, i for a peak/valley, its contribution is all the valid digits arrangements after i
                    sm += cws
            return ws, sm

        num = list(map(int, str(num)))
        n = len(num)
        return dfs(0, True, 0, 0, False)[1]
        
    def totalWaviness(self, num1: int, num2: int) -> int:
        a = self.countWaviness(num1-1)
        b = self.countWaviness(num2)

        return b - a
