class ST:
	def __init__(self, a):
		n = len(a)
		self.a = a
		self.tree = [0 for _ in range(4*n)]	# count of 1s
		self.lazy = [False for _ in range(4*n)] # pending flip
		self._build(0, 0, n)

	def _merge(self, lst, rst):
		return lst + rst

	def _apply(self, i, s, e):
		if self.lazy[i]:
			self.tree[i] = (e - s) - self.tree[i]   # updated 1s = len of segment - old 1s, since 0/1
			if e - s > 1:
				self.lazy[2*i+1] = not self.lazy[2*i+1]
				self.lazy[2*i+2] = not self.lazy[2*i+2]
			self.lazy[i] = False

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

	def update(self, i, s, e, l, r):
		self._apply(i, s, e)
		if s >= r or e <= l:
			return
		elif l <= s and e <= r:
			self.lazy[i] = True
			self._apply(i, s, e)
		else:
			m = s + (e - s) // 2
			self.update(2*i+1, s, m, l, r)
			self.update(2*i+2, m, e, l, r)
			self.tree[i] = self._merge(
				self.tree[2*i+1],
				self.tree[2*i+2]
			)


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        st = ST(nums1)
        n = len(nums1)
        s = sum(nums2)

        ans = []
        for x, y, z in queries:
            if x == 1:
                # update [y, z]
                st.update(0, 0, n, y, z+1)
            elif x == 2:
                # number of times p is added to the sum 
                # is the same as the number of 1s in nums1 at that point
                s += (y * st.tree[0])
            else:
                ans.append(s)

        return ans
