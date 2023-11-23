class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pairs, mx = {}, 1
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                if x1 == x2:
                    m = math.inf
                    b = x2
                else:
                    m = (y2 - y1) / (x2 - x1)
                    b = y2 - (m * x2)

                if (m, b) not in pairs:
                    pairs[(m, b)] = set()
                pairs[(m, b)].add((x1, y1))
                pairs[(m, b)].add((x2, y2))

                mx = max(mx, len(pairs[(m, b)]))

        print(pairs)
        # ans = (1 + math.sqrt(1 + 8 * mx)) / 2
        ans = mx

        return int(ans)
