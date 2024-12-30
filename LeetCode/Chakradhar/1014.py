class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, i = 0, 0
        for j in range(1, len(values)):
            ans = max(ans, values[i] + values[j] + i - j)
            if values[i] <= (values[j] + j - i):
                i = j

        return ans
