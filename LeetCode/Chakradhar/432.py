class ListNode:
    def __init__(self, val='', cnt=0, p=None, n=None):
        self.cnt, self.val = cnt, val
        self.p, self.n = p, n
    def __str__(self):
        node = self
        s = ''
        while node:
            s += f'({node.val}: {node.cnt})'
            node = node.n
        return s

class AllOne:

    def __init__(self):
        self.d = {}
        self.h, self.t = ListNode(), ListNode()
        self.h.p = self.t
        self.t.n = self.h

    def inc(self, key: str) -> None:
        if key not in self.d:
            self.d[key] = ListNode(val=key, cnt=0, p=self.t, n=self.t.n)
            self.t.n.p = self.d[key]
            self.t.n = self.d[key]
        node = self.d[key]
        node.cnt += 1
        while (node.n is not self.h) and (node.cnt > node.n.cnt):
            p0, p1, p2, p3 = node.p, node, node.n, node.n.n
            p0.n = p2
            p1.p, p1.n = p2, p3
            p2.p, p2.n = p0, p1
            p3.p = p1

    def dec(self, key: str) -> None:
        node = self.d[key]
        node.cnt -= 1
        if node.cnt == 0:
            p0, p2 = node.p, node.n
            p0.n = p2
            p2.p = p0
            del self.d[key]
            del node
        else:
            while (node.p is not self.t) and (node.cnt < node.p.cnt):
                p0, p1, p2, p3 = node.p.p, node.p, node, node.n
                p0.n = p2
                p1.p, p1.n = p2, p3
                p2.p, p2.n = p0, p1
                p3.p = p1

    def getMaxKey(self) -> str:
        return self.h.p.val

    def getMinKey(self) -> str:
        return self.t.n.val


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()