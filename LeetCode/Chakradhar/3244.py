from sortedcontainers import SortedList

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        sl = SortedList(range(n))
        ans, cur = [], n - 1
        for (u, v) in queries:
            torem = []
            for i in sl.irange(u, v, inclusive=(False, False)):
                torem.append(i)
            for i in torem:
                sl.discard(i)
                cur -= 1
            ans.append(cur)

        return ans
