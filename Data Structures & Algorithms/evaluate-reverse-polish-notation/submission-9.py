class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for item in tokens:
            if item in operators:
                # it means that we need to to the calculation:
                num2 = stack.pop()
                num1 = stack.pop()
                if item == '+':
                    new_num = (num1) + (num2)
                elif item == '-':
                    new_num = (num1) - (num2)
                elif item == '*':
                    new_num = (num1) * (num2)
                else:
                    new_num = int(float(num1) / (num2))

                stack.append(new_num)
            else:
                stack.append(int(item))
        
        return stack[-1]