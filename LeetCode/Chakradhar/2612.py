from sortedcontainers import SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned = set(banned + [p])
        even_rem, odd_rem = SortedList(), SortedList()
        l0, l1 = even_rem, odd_rem
        for i in range(n):
            if i not in banned:
                l0.add(i)
            l0, l1 = l1, l0

        ans = [-1 for _ in range(n)]
        q, d = deque([p]), 0
        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                ans[idx] = d

                left = max(0, idx - (k - 1))    # min start of window
                right = max(0, min(n - 1, idx + (k - 1)) - (k - 1)) # max start of window
                left = (left + (k - 1)) - (idx - left)  # where 1 would lie after reversing
                right = (right + (k - 1)) - (idx - right)   # where 1 would lie after reversing

                if left % 2:
                    rem = odd_rem
                else:
                    rem = even_rem
                pos_ids = list(rem.irange(left, right))

                for j in pos_ids:
                    q.append(j)
                    rem.remove(j)

            d += 1

        return ans
