class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        def good(x, y, a, b):
            return (x < a) and (y < b)

        n = len(nums1)
        row0 = [0, 1] # no flip, flip
        row1 = [0, 0]

        for i in range(1, n):
            x, y = nums1[i-1], nums2[i-1]
            a, b = nums1[i], nums2[i]

            # no flip
            if good(x, y, a, b):
                row1[0] = row0[0]
            else:
                row1[0] = math.inf
            if good(y, x, a, b):
                row1[0] = min(row1[0], row0[1])

            # flip
            if good(x, y, b, a):
                row1[1] = 1 + row0[0]
            else:
                row1[1] = math.inf
            if good(y, x, b, a):
                row1[1] = min(row1[1], 1 + row0[1])

            row0, row1 = row1, row0

        return min(row0)
