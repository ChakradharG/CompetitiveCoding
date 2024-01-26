class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        cur, suffix = 0, 0
        maxCur = 0
        for i in range(len(satisfaction)-1, -1, -1):
            cur += suffix + satisfaction[i]
            suffix += satisfaction[i]
            if maxCur > cur:
                break
            else:
                maxCur = cur

        return maxCur
