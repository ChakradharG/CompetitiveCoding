class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        grid0 = [[-math.inf for j in range(m+1)] for i in range(n+1)]
        grid1 = [[0 for j in range(m+1)] for i in range(n+1)]

        for _ in range(k):
            grid0[-1][-1] = -math.inf
            for i in reversed(range(n)):
                grid0[i][-1] = -math.inf
                for j in reversed(range(m)):
                    grid0[-1][j] = -math.inf
                    grid0[i][j] = max(
                        (nums1[i] * nums2[j]) + grid1[i+1][j+1],
                        grid0[i+1][j],
                        grid0[i][j+1],
                        grid0[i+1][j+1],
                    )
            grid0, grid1 = grid1, grid0

        return grid1[0][0]
