class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = {i+1: [0, [], 0] for i in range(n)}   # indeg, nei, start_time
        for (prv, nxt) in relations:
            adj[prv][1].append(nxt)
            adj[nxt][0] += 1

        q = deque([])
        for i in range(1, n+1):
            if adj[i][0] == 0:
                q.append((i, time[i-1]))    # course, end_time

        ans = 0
        while q:
            course, end_time = q.popleft()
            ans = max(ans, end_time)
            for nxt in adj[course][1]:
                adj[nxt][0] -= 1
                adj[nxt][2] = max(adj[nxt][2], end_time)
                if adj[nxt][0] == 0:
                    q.append((nxt, adj[nxt][2] + time[nxt-1]))

        return ans
