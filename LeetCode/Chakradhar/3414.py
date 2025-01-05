class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        def dfs(i, rem):
            if rem == 0 or i >= n:
                return 0, []

            key = (i, rem)
            if key not in memo:
                sc1, ids1 = dfs(i+1, rem)  # skip
                ids1 = ids1.copy()
                ids1.sort()

                l, r, w, x = intervals[i]
                j = bisect_right(intervals, r, lo=i+1, key=lambda x: x[0])
                sc2, ids2 = dfs(j, rem-1)
                ids2 = ids2.copy()
                sc2 += w
                ids2.append(x)
                ids2.sort()

                if sc1 > sc2:
                    memo[key] = sc1, ids1
                elif sc1 < sc2:
                    memo[key] = sc2, ids2
                else:
                    if ids1 < ids2:
                        memo[key] = sc1, ids1
                    else:
                        memo[key] = sc2, ids2
            return memo[key]

        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()
        memo = {}
        return sorted(dfs(0, 4)[1])
