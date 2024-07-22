class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def dfs(i, j):
            if (i == n1) or (j == n2):
                return -math.inf

            key = (i, j)
            if key not in memo:
                cur = nums1[i] * nums2[j]
                memo[key] = max(
                    cur + dfs(i+1, j+1),    # use i j and go further
                    cur,                    # use i j and stop here
                    dfs(i+1, j+1),          # skip both
                    dfs(i+1, j),            # skip i
                    dfs(i, j+1)             # skip j
                )

            return memo[key]

        n1, n2 = len(nums1), len(nums2)
        memo = {}
        return dfs(0, 0)
