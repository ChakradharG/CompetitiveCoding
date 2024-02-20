class ListNode:

    def __init__(self, val=None, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

    def __repr__(self):
        if self.r is None:  # tail
            n = self.l
            s = self.val if self.val is not None else ''
            while n.val:
                s = n.val + s
                n = n.l
        else:
            n = self.r
            s = ''
            while n.val:
                s += n.val
                n = n.r
        return s

class TextEditor:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode(l = self.head)
        self.head.r = self.tail
        self.cur = self.head

    def addText(self, text: str) -> None:
        right = self.cur.r
        for c in text:
            self.cur.r = ListNode(c, l=self.cur, r=right)
            self.cur = self.cur.r
        right.l = self.cur

    def deleteText(self, k: int) -> int:
        cnt = 0
        right = self.cur.r
        while (k > 0) and (self.cur.val is not None):
            self.cur.l.r = right
            self.cur = self.cur.l
            k -= 1
            cnt += 1
        right.l = self.cur
        return cnt

    def cursorLeft(self, k: int) -> str:
        while (k > 0) and (self.cur.val is not None):
            self.cur = self.cur.l
            k -= 1
        node, s, k = self.cur, '', 10
        while (node.val) and (k > 0):
            s = node.val + s
            node = node.l
            k -= 1
        return s

    def cursorRight(self, k: int) -> str:
        while (k > 0) and (self.cur.r.val is not None):
            self.cur = self.cur.r
            k -= 1
        node, s, k = self.cur, '', 10
        while (node.val) and (k > 0):
            s = node.val + s
            node = node.l
            k -= 1
        return s


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)