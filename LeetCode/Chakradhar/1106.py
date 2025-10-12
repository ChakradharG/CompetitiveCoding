class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        n = len(expression)
        ops = set('!&|')
        stack = []
        opstack = []

        def apply(a, b, op):
            if op == '&':
                return a & b
            elif op == '|':
                return a | b

        i = 0
        while i < n:
            if expression[i] == 't':
                stack.append(True)
            elif expression[i] == 'f':
                stack.append(False)
            elif expression[i] in ops:
                stack.append(expression[i])
                opstack.append(expression[i])
                i += 1
            elif expression[i] == ')':
                op = opstack.pop()
                cur = stack.pop()
                if op == '!':
                    cur = not cur
                else:
                    while stack[-1] not in ops:
                        cur = apply(cur, stack.pop(), op)
                stack.pop()
                stack.append(cur)
            i += 1

        return stack.pop()
