class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        nums.sort()
        # after sorting, nums[i] is the max for 2^i subseqs
        # and min for 2^(n-1-i) subseqs

        pows = [1] * n
        for i in range(1, n):
            pows[i] = (pows[i-1] * 2) % MOD

        ans = 0
        for i, num in enumerate(nums):
            ans = (ans + (num*pows[i] - num*pows[n-1-i])) % MOD

        return ans

