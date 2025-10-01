class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) - 1   # row index for pascal's triangle
        ans = nums[0]
        coeff = 1   # nC0

        for k in range(1, n+1):
            coeff = (coeff * (n - k + 1) // k) # nCk-1 -> nCk
            ans = (ans + coeff * nums[k]) % 10

        return ans
