class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        row0 = [0 for _ in range(4)]
        row1 = [0 for _ in range(4)]

        for i in range(len(prices)-1, -1, -1):
            row0[3] = max(prices[i] + row1[0], row1[3])
            row0[2] = max(prices[i], row1[2])
            row0[1] = max(row1[3] - prices[i], row1[1])
            row0[0] = max(row1[2] - prices[i], row1[0])

            row0, row1 = row1, row0

        return row1[1]
