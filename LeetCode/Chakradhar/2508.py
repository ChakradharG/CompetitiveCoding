class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n+1)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        odd = []
        for u in range(1, n+1):
            if len(graph[u]) % 2:
                odd.append(u)

        match len(odd):
            case 0:
                return True
            case 2:
                if odd[1] not in graph[odd[0]]:
                    return True
                for u in range(1, n+1):
                    if u == odd[0] or u == odd[1]:
                        continue
                    if (u not in graph[odd[0]]) and (u not in graph[odd[1]]):
                        return True
                return False
            case 4:
                return (
                    ((odd[0] not in graph[odd[1]]) and (odd[2] not in graph[odd[3]])) or
                    ((odd[0] not in graph[odd[2]]) and (odd[1] not in graph[odd[3]])) or
                    ((odd[0] not in graph[odd[3]]) and (odd[2] not in graph[odd[1]]))
                )
            case _:
                return False

