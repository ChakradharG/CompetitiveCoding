class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        bits = []   #LSB -> MSB (order reversed)
        while n:
            bits.append(n & 0b01)
            n >>= 1

        cost = {}
        def setBit(idx, val):
            if bits[idx] == val:
                return 0

            bits[idx] = val

            if idx == 0:
                return 1

            key = (idx, tuple(bits))
            if key in cost:
                return cost[key]

            c = setBit(idx - 1, 1)
            if c != 0:
                cost[key] = 1 + c + (2**(idx-1) - 1)
            else:
                cost[key] = 1 + c
                for i in range(idx-2, -1 ,-1):
                    c = setBit(i, 0)
                    if c != 0:
                        cost[key] += c + (2**i - 1)
                        break

            return cost[key]

        if sum(bits) == 1:
            ans = 0
            x = len(bits)
        else:
            ans = setBit(len(bits)-1, 0)
            x = len(bits) - 1

        ans += (2**x - 1)
        return ans