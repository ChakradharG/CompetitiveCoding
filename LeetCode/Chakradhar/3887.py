class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        def union(a, b, w):
            (a, pa), (b, pb) = find(a), find(b)
            x = pa ^ pb ^ w
            if a != b:
                parent[b] = a
                parity[b] = x
                return 1
            else:
                if x:
                    return 0
                else:
                    return 1

        def find(a):
            if parent[a] == a:
                return [a, 0]
            A, p = find(parent[a])
            parent[a] = A
            parity[a] ^= p
            return [parent[a], parity[a]]

        parent = [i for i in range(n)]
        parity = [0 for i in range(n)]

        ans = 0
        for u, v, w in edges:
            ans += union(u, v, w)

        return ans
