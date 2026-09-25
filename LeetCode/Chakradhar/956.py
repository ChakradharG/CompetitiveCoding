class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        n = len(rods)
        s = sum(rods)
        m = 2 * s + 1
        row0 = [0] * m
        row1 = [-inf] * s + [0] + [-inf] * s

        for i in reversed(range(n)):
            for diff in range(rods[i], m-rods[i]):
                row0[diff] = max(
                    row1[diff],
                    row1[diff+rods[i]] + rods[i],
                    row1[diff-rods[i]]
                )
            row0, row1 = row1, row0
        return row1[s]

