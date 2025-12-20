class Solution:
    def lastInteger(self, n: int) -> int:
        a, d, e = 1, 1, n
        ltor = True
        while n > 1:
            if ltor:
                if n % 2 == 0:
                    e -= d
            else:
                if n % 2 == 0:
                    a += d
            d *= 2
            n = math.ceil(n / 2)
            ltor = not ltor

        return a
