class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + stones[i]

        score_diff = pref[n-1]
        for i in reversed(range(1, n-1)):
            score_diff = max(
                score_diff, # skip
                pref[i] - score_diff # pick
            )

        return score_diff

