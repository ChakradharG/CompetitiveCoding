class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k2 = k * 2
        row0 = [0 for _ in range(k2)]
        row1 = [0 for _ in range(k2)]

        for i in range(len(prices)-1, -1, -1):
            for j in range(k):
                row0[j] = max(row1[k+j] - prices[i], row1[j])
            row0[k] = max(prices[i], row1[k])
            for j in range(k+1, k2):
                row0[j] = max(prices[i] + row1[j-(k+1)], row1[j])

            row0, row1 = row1, row0

        return row1[k-1]