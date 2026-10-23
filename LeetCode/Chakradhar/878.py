@cache
def lcm(a: int, b: int) -> int:
    res = a * b
    while b:
        a, b = b, a % b
    return res // a


class Solution:
    def countDivisible(self, x: int, divs: List[int]) -> int:
        k = len(divs)
        cnt = 0
        for mask in range(1, 1 << k):
            l = 1
            for i in range(k):
                if (mask >> i) & 1:
                    l = lcm(l, divs[i])
                    if l > x:
                        break
            sign = 1 if bin(mask).count('1') % 2 else -1
            cnt += sign * (x // l)
        return cnt

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        l, r = 1, n * min(a, b)
        while l < r:
            m = l + (r - l) // 2
            cnt = self.countDivisible(m, [a, b])
            if cnt < n:
                l = m + 1
            elif cnt >= n:
                r = m

        return r % MOD

