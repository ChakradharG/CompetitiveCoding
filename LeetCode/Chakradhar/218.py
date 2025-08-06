class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        line = []
        for l, r, h in buildings:
            line.append((l, -h))
            line.append((r, h))
        heapify(line)

        toRem = defaultdict(int)
        h = [0]
        cur = 0
        ans = []

        while line:
            x, d = heappop(line)
            if d < 0:
                heappush(h, d)
            else:
                toRem[-d] += 1

            while toRem[h[0]] != 0:
                toRem[heappop(h)] -= 1

            if cur != -h[0]:
                cur = -h[0]
                ans.append((x, cur))

        return ans
