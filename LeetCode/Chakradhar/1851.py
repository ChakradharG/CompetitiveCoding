class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        line = []   # coord, type (0->open, 1->query, 2->close)
        for i, (l, r) in enumerate(intervals):
            line.append((l, 0, i))
            line.append((r, 2, i))
        for i, q in enumerate(queries):
            line.append((q, 1, i))
        line.sort()

        opn = [] # size, index
        cur = set() # currently open interval indices (from intervals)
        ans = [-1 for _ in range(len(queries))]
        for j in range(len(line)):
            i = line[j][2]
            if line[j][1] == 0:
                l, r = intervals[i]
                cur.add(i)
                heappush(opn, (r - l + 1, i))
            elif line[j][1] == 2:
                cur.remove(i)
                while opn and opn[0][1] not in cur:
                    heappop(opn)
            else:
                if len(opn) != 0:
                    ans[i] = opn[0][0]

        return ans
