class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0]) # sort by start time

        nxt = []    # next available event after event `i`
        for i in range(n):
            j = bisect_right(events, events[i][1], key=lambda x: x[0])
            nxt.append(j)

        row0 = [0 for _ in range(n+1)]
        row1 = [0 for _ in range(n+1)]

        for _ in range(k):
            for i in reversed(range(n)):
                row0[i] = max(
                    row0[i+1], # skip
                    events[i][2] + row1[nxt[i]]
                )
            row0, row1 = row1, row0

        return row1[0]
