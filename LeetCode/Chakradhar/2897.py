class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        grid = [["0" for j in range(32)] for i in range(n)]
        ptrs = [0] * 32

        # let's assume i gets the AND value and j gets the OR value
        # this operation can be visualized as transferring bits that
        # are set in i but not in j

        # columnwise pushing the ones to the top, to maximize the top vals
        for i in range(n):
            x = bin(nums[i])[:1:-1]
            for j in range(len(x)):
                if x[j] == "1":
                    grid[ptrs[j]][j] = "1"
                    ptrs[j] += 1

        ans = 0
        MOD = 10**9 + 7
        for i in range(k):
            num = int("".join(grid[i][::-1]), 2)
            ans = (ans + pow(num, 2, MOD)) % MOD

        return ans

