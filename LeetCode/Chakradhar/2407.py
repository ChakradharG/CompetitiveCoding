class ST:
    def __init__(self, n):
        self.tree = [0 for _ in range(4*n)]

    def _merge(self, lst, rst):
        return max(lst, rst)

    def query(self, i, s, e, l, r):
        if s >= r or e <= l:
            return 0
        elif l <= s and e <= r:
            return self.tree[i]
        else:
            m = s + (e - s) // 2
            return self._merge(
                self.query(2*i+1, s, m, l, r),
                self.query(2*i+2, m, e, l, r)
            )

    def update(self, i, s, e, l, d):
        if l < s or e <= l:
            return
        elif e - s == 1 and s == l:
            self.tree[i] = d
        else:
            m = s + (e - s) // 2
            self.update(2*i+1, s, m, l, d)
            self.update(2*i+2, m, e, l, d)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums) + 1
        st = ST(n)

        ans = 0
        for num in nums:
            x = 1 + st.query(0, 0, n, num-k, num)
            ans = max(ans, x)
            st.update(0, 0, n, num, x)

        return ans
