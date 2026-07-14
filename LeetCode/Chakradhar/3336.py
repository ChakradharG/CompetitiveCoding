class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        @cache
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        @cache
        def dfs(i, seq1, seq2):
            areEq = 0
            if seq1 != 0 and seq1 == seq2:
                areEq = 1
            if i == n:
                return areEq
            return (
                + dfs(i+1, seq1, seq2)
                + dfs(i+1, gcd(seq1, nums[i]), seq2)
                + dfs(i+1, seq1, gcd(seq2, nums[i]))
            ) % MOD

        n = len(nums)
        MOD = 10**9 + 7

        return dfs(0, 0, 0)

