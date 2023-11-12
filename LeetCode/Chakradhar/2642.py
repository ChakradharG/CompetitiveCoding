class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adjList = {i: [] for i in range(n)}
        for (src, dst, cost) in edges:
            self.adjList[src].append((dst, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.adjList[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        print('hi')
        visited, distance = set(), [math.inf for i in range(self.n)]

        distance[node1] = 0
        # heapq.heapify(distance)
        for i in range(self.n):
            # u = heapq.heappop(distance)
            # while u in visited:
            #     u = heapq.heappop(distance)
            mn, u = math.inf, -1
            for i in range(len(distance)):
                if (distance[i] < mn) and (i not in visited):
                    mn, u = distance[i], i
            print(visited, u)
            if u == -1:
                return -1
            visited.add(u)
            for (v, cost) in self.adjList[u]:
                # if v in visited:
                #     continue
                distance[v] = min(distance[v], distance[u] + cost)
            if node2 in visited:
                break

        return distance[node2]



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)