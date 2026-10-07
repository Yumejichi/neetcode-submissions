class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for i in range(len(tokens)):
            if tokens[i] in operations:
                second = stack.pop()
                first = stack.pop()
                if tokens[i] == "+":
                    stack.append(first + second)
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(first * second)
                elif tokens[i] == "/":
                    stack.append(int(first / second))
            else:
                stack.append(int(tokens[i]))
        return stack[0]

