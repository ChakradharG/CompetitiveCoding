class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def get_neighbors(u):
            if len(groups[arr[u]]) > 0:
                for v in groups[arr[u]]:
                    if v not in enqd:
                        yield v
                del groups[arr[u]]
            if u-1 not in enqd:
                yield u-1
            if u+1 not in enqd:
                yield u+1

        n = len(arr)
        groups = defaultdict(set)
        for i, num in enumerate(arr):
            groups[num].add(i)

        q = deque([0])
        enqd = {0, -1, n}
        steps = 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if u == n-1:
                    return steps
                for v in get_neighbors(u):
                    q.append(v)
                    enqd.add(v)
            steps += 1

        return steps
