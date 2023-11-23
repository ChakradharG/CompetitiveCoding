class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxPts = 1
        slopes = {}
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x1 == x2:
                    slope = math.inf
                    intercept = x2
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    intercept = y2 - (slope * x2)
                if (slope, intercept) not in slopes:
                    slopes[(slope, intercept)] = set()
                slopes[(slope, intercept)].add((x1, y1))
                slopes[(slope, intercept)].add((x2, y2))
                maxPts = max(maxPts, len(slopes[(slope, intercept)]))

        print(slopes)
        return maxPts
