class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        bits = []   #LSB -> MSB (order reversed)
        while n:
            bits.append(n & 0b01)
            n >>= 1

        def setBit(idx, val):
            if bits[idx] == val:
                return 0

            bits[idx] = val

            if idx == 0:
                return 1

            cost = setBit(idx - 1, 1)
            if cost != 0:   # meaning it is now of the form x...11x...
                cnt = 1 + cost + (2**(idx-1) - 1)
            else:
                cnt = 1 + cost
                for i in range(idx-2, -1 ,-1):
                    cost = setBit(i, 0)
                    if cost != 0: # meaning it is now of the form x...01x...
                        cnt += cost + (2**i - 1)
                        break

            return cnt

        if sum(bits) == 1:
            ans = 2**len(bits) - 1
        else:
            ans = setBit(len(bits) - 1, 0) + 2**(len(bits) - 1) - 1

        return ans