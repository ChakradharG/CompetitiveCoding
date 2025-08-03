class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        s = bisect_left(fruits, startPos, key=lambda x:x[0])
        suff = [0 for _ in range(k+1)]
        i = s
        while i < len(fruits):
            j = fruits[i][0] - startPos
            if j > k:
                break
            suff[j] += fruits[i][1]
            i += 1

        for i in range(1, len(suff)):
            suff[i] += suff[i-1]

        ans = suff[-1]
        i = s - 1
        cur = 0
        while i > -1:
            cur += fruits[i][1]
            steps = startPos - fruits[i][0]
            if steps > k:
                break
            ans = max(
                ans,
                cur + suff[max(0, k - 2*steps)],        # left then right
                cur + suff[max(0, (k - steps) // 2)]    # right then left
            )
            i -= 1

        return ans
