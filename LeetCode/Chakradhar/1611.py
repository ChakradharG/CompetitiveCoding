class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        nBits = math.floor(math.log2(n)) + 1

        def assignBit(idx, val):
            nonlocal n
            if ((n >> idx) & 0b1) == val:
                return 0

            # setting/resetting bit
            if val:
                n |= (1 << idx)
            else:
                n &= ~(1 << idx)

            if idx == 0:
                return 1

            cost = assignBit(idx - 1, 1)
            if cost != 0:   # meaning it is now of the form x...11x...
                cnt = 1 + cost + (2**(idx-1) - 1)
            else:
                cnt = 1 + cost
                for i in range(idx-2, -1 ,-1):
                    cost = assignBit(i, 0)
                    if cost != 0: # meaning it is now of the form x...01x...
                        cnt += cost + (2**i - 1)
                        break

            return cnt

        if (math.log2(n) % 1) == 0:
            ans = 2**nBits - 1
        else:
            ans = assignBit(nBits-1, 0) + (2**(nBits-1) - 1)

        return ans