class Solution:
    """
    Postfix - operators follow their operands
    """
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
   
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append((int(token)))
            else:

                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    stack.append(int(operand1 / operand2))
        return stack.pop()