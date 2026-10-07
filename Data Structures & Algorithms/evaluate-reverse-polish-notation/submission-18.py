class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for i in range(len(tokens)):
            if tokens[i] in operations:
                if stack:
                    second = stack.pop()
                if stack:
                    first = stack.pop()
                # if first and second:# 0 is false so we remove this line
                # if anything happens, the above lines already catches the error
                if tokens[i] == "+":
                    stack.append(first + second)
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(int(first * second))
                elif tokens[i] == "/":
                    stack.append(int(first / second))
            else:
                stack.append(int(tokens[i]))
        return stack[0]

