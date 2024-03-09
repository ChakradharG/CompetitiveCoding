class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        def updateScores(beg, end): # [beg, end)
            scores[beg] += 1
            if end != n:
                scores[end] -= 1

        n = len(nums)
        scores = [0 for _ in range(n)]
        for i, num in enumerate(nums):
            if num == 0:    # scoring for any k
                updateScores(0, n)
            elif num <= i:    # already scoring
                updateScores(0, i - num + 1)
                if i != (n - 1):
                    # if already scoring and not the last, then scoring in 
                    # 2 index ranges: [num, i+1) and [i+1, n)
                    updateScores(i + 1, n)
            else:
                updateScores(
                    i + 1, 
                    (n - num) + i + 1
                )

        ans = [0, scores[0]]  # idx, score
        for i in range(1, len(scores)):
            scores[i] += scores[i-1]
            if scores[i] > ans[1]:
                ans = [i, scores[i]]

        return ans[0]
        