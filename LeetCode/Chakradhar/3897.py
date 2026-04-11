class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        def f(x):
            nonlocal ans
            o, z = x
            if z == 0:
                # if no 0's, directly append it to ans
                ans = ((ans << o) + (2**o - 1)) % MOD
                return False
            else:
                return True

        ans = 0
        MOD = 10**9 + 7
        for o, z in sorted(filter(f, zip(nums1, nums0)), key=lambda x: (-x[0], x[1])):
            ans = ((ans << o) + (2**o - 1)) % MOD
            ans = (ans << z) % MOD

        return ans
