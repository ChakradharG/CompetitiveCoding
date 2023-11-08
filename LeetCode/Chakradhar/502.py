class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalHeap = [(c, p) for (p, c) in zip(profits, capital)]
        heapq.heapify(capitalHeap)
        profitHeap = []

        while k > 0:
            while capitalHeap and capitalHeap[0][0] <= w:
                heapq.heappush(
                    profitHeap,
                    -heapq.heappop(capitalHeap)[1]
                )

            if profitHeap:
                w -= heapq.heappop(profitHeap)
            else:
                break
            k -= 1

        return w
