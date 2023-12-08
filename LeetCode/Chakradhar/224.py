class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(y, op, x):
            if op == '+':
                return int(x) + int(y)
            else:
                return int(x) - int(y)

        def calcGrp(idx):
            while s[idx] == ' ':
                idx += 1

            if s[idx] == '-':
                stack = [0]
            else:
                stack = []

            while s[idx] != ')':
                if s[idx] == ' ':
                    pass
                elif s[idx] == '(':
                    val, idx = calcGrp(idx+1)
                    stack.append(val)
                elif s[idx] == '+' or s[idx] == '-':
                    if len(stack) == 3:
                        stack.append(evaluate(
                            stack.pop(), 
                            stack.pop(), 
                            stack.pop()
                        ))
                    stack.append(s[idx])
                else:
                    if stack and str.isnumeric(stack[-1]):
                        stack.append(
                            stack.pop() + s[idx]
                        )
                    else:
                        stack.append(s[idx])

                idx += 1

            if len(stack) == 1:
                return int(stack.pop()), idx
            else:
                return evaluate(stack.pop(), stack.pop(), stack.pop()), idx

        s += ')'
        return calcGrp(0)[0]
