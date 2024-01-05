class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        LIS = []
        ans = [1 for _ in range(len(obstacles))]
        for i in range(len(obstacles)):
            idx = bisect.bisect(LIS, obstacles[i])
            ans[i] = idx + 1
            if idx == len(LIS):
                LIS.append(obstacles[i])
            else:
                LIS[idx] = obstacles[i]

        return ans
