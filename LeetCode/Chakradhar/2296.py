class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        cnt = 0
        while (k > 0) and self.left:
            self.left.pop()
            k, cnt = k - 1, cnt + 1
        return cnt

    def cursorLeft(self, k: int) -> str:
        while (k > 0) and self.left:
            self.right.append(self.left.pop())
            k -= 1
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        while (k > 0) and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return ''.join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)