class ST:
	def __init__(self, a):
		self.a = a
		n = len(a)
		self.tree = [0 for _ in range(4*n)]	# range sum
		self.lazy = [0 for _ in range(4*n)]
		self._build(0, 0, n)

	def _merge(self, lst, rst):
		return lst + rst

	def _apply(self, i, s, e):
		# apply lazy update and propagate downwards
		if self.lazy[i] != 0:
			# pending lazy update
			self.tree[i] += (e - s) * self.lazy[i] # i tracks to e-s indices
			if e - s > 1:
				# not a leaf node, need to propagate the update to children
				self.lazy[2*i+1] += self.lazy[i]
				self.lazy[2*i+2] += self.lazy[i]
			self.lazy[i] = 0 # reset

	def _build(self, i, s, e):
		if e - s == 1:
			self.tree[i] = self.a[s]
		else:
			m = (s + e) // 2
			self._build(2*i+1, s, m)
			self._build(2*i+2, m, e)
			self.tree[i] = self._merge(
				self.tree[2*i+1],
				self.tree[2*i+2]
			)

	def query(self, i, s, e, l, r):
		# point query would have r = l+1
		self._apply(i, s, e)
		if s >= r or e <= l:
			return 0
		elif l <= s and e <= r:
			return self.tree[i]
		else:
			m = (s + e) // 2
			return self._merge(
				self.query(2*i+1, s, m, l, r),
				self.query(2*i+2, m, e, l, r)
			)

	def update(self, i, s, e, l, r, d):
		# point update would have r = l+1
		# d = new val - old val, i.e., the delta and not new val
		self._apply(i, s, e)
		if s >= r or e <= l:
			return
		elif l <= s and e <= r:
			self.lazy[i] = d
			self._apply(i, s, e)
		else:
			m = (s + e) // 2
			self.update(2*i+1, s, m, l, r, d)
			self.update(2*i+2, m, e, l, r, d)
			self.tree[i] = self._merge(
				self.tree[2*i+1],
				self.tree[2*i+2]
			)