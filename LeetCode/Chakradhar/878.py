@cache
def lcm(a: int, b: int) -> int:
    res = a * b
    while b:
        a, b = b, a % b
    return res // a


class Solution:
    def countDivisible(self, x: int, divs: List[int]) -> int:
        a, b = divs
        return x//a + x//b - x//lcm(a, b)

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        l, r = 1, n * min(a, b)
        while l < r:
            m = l + (r - l) // 2
            if self.countDivisible(m, [a, b]) < n:
                l = m + 1
            else:
                r = m

        return r % MOD

