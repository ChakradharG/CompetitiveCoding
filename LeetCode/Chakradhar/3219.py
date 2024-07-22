class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        cuts = sorted(
            [(c, 'h') for c in horizontalCut] +
            [(c, 'v') for c in verticalCut],
            reverse=True
        )

        h, v = 1, 1
        ans = 0
        for (c, d) in cuts:
            if d == 'h':
                ans += (c * h)
                v += 1
            else:
                ans += (c * v)
                h += 1

        return ans