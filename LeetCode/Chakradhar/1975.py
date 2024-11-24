class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n, p = [], []
        for row in matrix:
            for num in row:
                if num < 0:
                    n.append(num)
                else:
                    p.append(num)

        ans = sum(p)
        if len(n) % 2 == 0:
            ans -= sum(n)
        else:
            x = min(p, default=math.inf)
            y = max(n)
            if abs(y) > x:
                ans -= sum(n)
                ans -= x
                ans -= x
            else:
                ans -= sum(n)
                ans += y
                ans += y

        return ans
