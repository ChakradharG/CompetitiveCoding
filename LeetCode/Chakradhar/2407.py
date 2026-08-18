class ST:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(2*n)]

    def _merge(self, lst, rst):
        return max(lst, rst)

    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1:
                res = self._merge(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self._merge(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

    def update(self, l, d):
        i = l + self.n
        self.tree[i] = d
        while (i := (i >> 1)) > 0:
            x = self._merge(self.tree[2*i], self.tree[2*i+1])
            if self.tree[i] == x:
                break
            self.tree[i] = x


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums) + 1
        st = ST(n)

        ans = 0
        for num in nums:
            x = 1 + st.query(max(0, num-k), num)
            ans = max(ans, x)
            st.update(num, x)

        return ans

