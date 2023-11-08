class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        merged = sorted([
            (-p, c) for (p, c) in zip(profits, capital)
        ], key=lambda x: x[1])

        heap = []
        mptr = 0
        while k > 0:
            while mptr < len(merged) and merged[mptr][1] <= w:
                heapq.heappush(heap, merged[mptr])
                mptr += 1

            if heap:
                w -= heapq.heappop(heap)[0]
            else:
                break
            k -= 1

        return w
