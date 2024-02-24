class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = {i: [math.inf, []] for i in range(n)} # [t, nei]
        for (x, y, t) in meetings:
            adj[x][1].append((y, t))
            adj[y][1].append((x, t))
        adj[0][1].append((firstPerson, 0))

        q = deque([0])
        adj[0][0] = 0
        while q:
            x = q.popleft()
            for (y, t) in adj[x][1]:
                if t >= adj[x][0]: # x has secret at the time of meeting y
                    if t < adj[y][0]:  # found a way to get secret to y (faster)
                        adj[y][0] = t
                        q.append(y)

        return [k for k, v in adj.items() if v[0] != math.inf]
