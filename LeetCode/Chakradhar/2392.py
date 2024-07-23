class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological(conds):
            ideg = {i: 0 for i in nums}
            odeg = {i: [] for i in nums}
            for u, v in conds:
                ideg[v] += 1
                odeg[u].append(v)

            q = deque([])
            order, cnt = {}, 0
            for u in nums:
                if ideg[u] == 0:
                    q.append(u)
                    order[u] = cnt
                    cnt += 1

            while q:
                u = q.popleft()
                for v in odeg[u]:
                    ideg[v] -= 1
                    if ideg[v] == 0:
                        q.append(v)
                        order[v] = cnt
                        cnt += 1

            if cnt != k:    # cycles
                return None
            else:
                return order

        nums = list(range(1, k+1))

        rows = topological(rowConditions)
        cols = topological(colConditions)
        if rows is None or cols is None:
            # not possible
            return []

        ans = [[0 for j in range(k)] for i in range(k)]
        for num in nums:
            i, j = rows[num], cols[num]
            ans[i][j] = num

        return ans
