class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def forwardOr(num):
            num = ('0' * (32 - len(num))) + num
            cur = 0
            for i in range(32):
                cur <<= 1
                bits[i] += (num[i] == '1')
                cur += (bits[i] > 0)
            return cur

        def backwardOr(num):
            num = ('0' * (32 - len(num))) + num
            cur = 0
            for i in range(32):
                cur <<= 1
                bits[i] -= (num[i] == '1')
                cur += (bits[i] > 0)
            return cur

        bits = [0 for _ in range(32)]

        l, r = 0, 0
        cur, ans = 0, math.inf

        while r < len(nums):
            cur = forwardOr(bin(nums[r])[2:])

            while l <= r and cur >= k:
                ans = min(ans, r - l + 1)
                cur = backwardOr(bin(nums[l])[2:])
                l += 1

            r += 1

        if ans == math.inf:
            return -1
        return ans
