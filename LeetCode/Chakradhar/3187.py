class ST:
    def __init__(self, a):
        self.a = a
        n = len(a)
        self.tree = [0 for _ in range(4*n)]
        self._build(0, 0, n)

    def _merge(self, lst, rst):
        return lst + rst

    def _build(self, i, s, e):
        if e - s == 1:
            self.tree[i] = self.a[s]
        else:
            m = s + (e - s) // 2
            self._build(2*i+1, s, m)
            self._build(2*i+2, m, e)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )

    def query(self, i, s, e, l, r):
        if s >= r or l >= e:
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
        if e - s == 1:
            self.a[s] = d
            self.tree[i] = d
        else:
            m = s + (e - s) // 2
            if l < m:
                self.update(2*i+1, s, m, l, d)
            else:
                self.update(2*i+2, m, e, l, d)
            self.tree[i] = self._merge(
                self.tree[2*i+1],
                self.tree[2*i+2]
            )

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        peak = [0 for _ in range(n)]
        for i in range(1, n-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                peak[i] = 1
        st = ST(peak)

        ans = []
        for q in queries:
            if q[0] == 1:
                if q[1] == q[2]:
                    # single element subarray
                    ans.append(0)
                else:
                    ans.append(
                        st.query(0, 0, n, q[1], q[2]+1)
                        - peak[q[1]]
                        - peak[q[2]]
                    )   # since first and last elements of subarray can't be peaks (even if they are peaks when the entire array is considered)
            else:
                i = q[1]
                nums[i] = q[2]
                if 0 < i < n-1:
                    peak[i] = int(nums[i-1] < nums[i] > nums[i+1])
                    st.update(0, 0, n, i, peak[i])
                if i > 1:
                    peak[i-1] = int(nums[i-2] < nums[i-1] > nums[i])
                    st.update(0, 0, n, i-1, peak[i-1])
                if i < n-2:
                    peak[i+1] = int(nums[i] < nums[i+1] > nums[i+2])
                    st.update(0, 0, n, i+1, peak[i+1])

        return ans
