class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjList = [[] for _ in range(n)]
        for (src, dst, cost) in edges:
            self.adjList[src].append((dst, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.adjList[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        visited = [math.inf for _ in range(len(self.adjList))]
        visited[node1] = 0
        distance = [(0, node1)]

        while distance:
            dist, u = heapq.heappop(distance)
            if visited[u] != math.inf and visited[u] != 0:
                continue
            if u == node2:
                return dist

            visited[u] = dist
            for (v, cost) in self.adjList[u]:
                # if v in visited:
                #     continue
                heapq.heappush(distance, (dist + cost, v))
            # if node2 in visited:
            #     break

        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)