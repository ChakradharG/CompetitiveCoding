class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts = [0 for _ in range(n)]
        vacant = list(range(n))
        occupied = []

        meetings.sort(key=lambda x: x[0])
        for (st, et) in meetings:
            while occupied and occupied[0][0] <= st:
                _, room = heapq.heappop(occupied)
                heapq.heappush(vacant, room)
            if vacant:
                room = heapq.heappop(vacant)
                off = 0
            else:
                pet, room = heapq.heappop(occupied)
                off = (pet - st)
            counts[room] += 1
            heapq.heappush(occupied, (et + off, room))

        ans = [counts[n-1], n-1]
        for i in range(n-1, -1, -1):
            if counts[i] >= ans[0]:
                ans = [counts[i], i]

        return ans[1]
