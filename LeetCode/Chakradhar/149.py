class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxPts = 1
        for i in range(len(points)-1):
            slopes = {}
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                if x1 == x2:
                    m = math.inf
                else:
                    m = (y2 - y1) / (x2 - x1)

                if m not in slopes:
                    slopes[m] = 0
                slopes[m] += 1

                maxPts = max(maxPts, slopes[m] + 1)

        return maxPts