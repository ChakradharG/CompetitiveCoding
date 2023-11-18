class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjList = [[] for _ in range(n)]
        for (src, dst, cost) in edges:
            self.adjList[src].append((dst, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.adjList[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        distance = [math.inf for _ in range(len(self.adjList))]
        distance[node1] = 0
        priQ = [(0, node1)]

        while priQ:
            dist, u = heapq.heappop(priQ)
            if dist > distance[u]:
                continue
            if u == node2:
                return dist

            for (v, cost) in self.adjList[u]:
                newDist = dist + cost
                if newDist < distance[v]:
                    distance[v] = newDist
                    heapq.heappush(priQ, (newDist, v))

        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)