class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = {i: [] for i in range(n)}
        for (x, y, t) in meetings:
            adj[x].append((y, t))
            adj[y].append((x, t))
        adj[0].append((firstPerson, 0))

        q = deque([0])
        vis = {0: 0}
        while q:
            x = q.popleft()
            for (y, t) in adj[x]:
                if t >= vis[x]: # x has secret at the time of meeting y
                    if y not in vis or vis[y] > t:  # found a way to get secret to y (faster)
                        vis[y] = t
                        q.append(y)

        return vis.keys()
