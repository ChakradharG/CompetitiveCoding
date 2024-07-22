class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        row0 = [-math.inf for _ in range(n+1)]
        row1 = [-math.inf for _ in range(n+1)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                cur = nums1[i] * nums2[j]
                row0[j] = max(
                    cur + row1[j+1],    # use i j and go further
                    cur,                # use i j and stop here
                    row1[j+1],          # skip both
                    row1[j],            # skip i
                    row0[j+1]           # skip j
                )
            row0, row1 = row1, row0

        return row1[0]
