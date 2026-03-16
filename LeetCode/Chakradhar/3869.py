class Solution:
    def getDigits(self, num):
        return [int(d) for d in str(num)]
    def isGoodInc(self, cur):
        cur = self.getDigits(cur)
        for i in range(len(cur)-1):
            if cur[i] >= cur[i+1]:
                return False
        return True
    def isGoodDec(self, cur):
        cur = self.getDigits(cur)
        for i in range(len(cur)-1):
            if cur[i] <= cur[i+1]:
                return False
        return True
    def countGood(self, num):
        num = self.getDigits(num)
        n = len(num)
        @cache
        def dfs(i, tight, prv, direc, cur):
            if i == n:
                if direc == 0:
                    return int(self.isGoodInc(cur) or self.isGoodDec(cur))
                else:
                    return 1
            r = num[i] if tight else 9
            res = 0
            for d in range(r+1):
                t = tight and (d == num[i])
                c = cur + d
                if prv == -1:
                    if d == 0:
                        res += dfs(i+1, t, -1, 0, c)
                    else:
                        res += dfs(i+1, t, d, 2, c) # only 1 digit places, direc undecided
                else:
                    if d != prv and direc == 2:
                        if d < prv:
                            res += dfs(i+1, t, d, -1, c)
                        elif d > prv:
                            res += dfs(i+1, t, d, +1, c)
                    elif d < prv and direc == -1:
                            res += dfs(i+1, t, d, -1, c)
                    elif d > prv and direc == +1:
                            res += dfs(i+1, t, d, +1, c)
                    else:
                        res += dfs(i+1, t, d, 0, c)
            return res
        return dfs(0, True, -1, 0, 0)
    def countFancy(self, l: int, r: int) -> int:
        return self.countGood(r) - self.countGood(l-1)

