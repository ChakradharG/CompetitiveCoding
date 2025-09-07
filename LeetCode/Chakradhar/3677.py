class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        def mirror(high, bitlen):
            s = bin(high)[2:]
            if bitlen % 2 == 0:
                m = s + s[::-1]
            else:
                m = s + s[-2::-1]
            return int(m, 2)

        if n == 0:
            return 1
        elif n == 1:
            return 2
        elif n == 2:
            return 2
        elif n == 3:
            return 3

        bitlen = len(bin(n)) - 2
        ans = 3

        for l in range(3, bitlen):
            cur = pow(2, (l // 2) - 1)
            if l % 2 == 1:
                cur *= 2
            ans += cur

        halflen = (bitlen + 1) // 2
        high = n >> (bitlen - halflen)
        low = 1 << (halflen - 1)
        ans += max(0, high - low)

        if mirror(high, bitlen) <= n:
            ans += 1

        return ans
