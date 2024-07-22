class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        m, n = m - 1, n - 1
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        h, v = 1, 1
        i, j = 0, 0

        ans = 0
        while i < m and j < n:
            if horizontalCut[i] >= verticalCut[j]:
                ans += (horizontalCut[i] * h)
                v += 1
                i += 1
            else:
                ans += (verticalCut[j] * v)
                h += 1
                j += 1

        while i < m:
            ans += (horizontalCut[i] * h)
            i += 1
        while j < n:
            ans += (verticalCut[j] * v)
            j += 1

        return ans