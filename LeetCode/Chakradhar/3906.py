class Solution:
    def count(self, num, path):
        num = list(map(int, str(num)))
        num = [0] * (16 - len(num)) + num
        n = 16

        @cache
        def dfs(i, tight, prv):
            if i == n:
                return 1
            l = prv if i in path else 0
            r = num[i] if tight else 9
            res = 0
            for d in range(l, r+1):
                res += dfs(i+1, tight and (d == num[i]), d if i in path else prv)
            return res

        return dfs(0, True, 0)

    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        path = {0}
        y, x = 0, 0
        for d in directions:
            match d:
                case 'R':
                    x += 1
                case 'D':
                    y += 1
            path.add(4*y + x)

        return self.count(r, path) - self.count(l-1, path)
