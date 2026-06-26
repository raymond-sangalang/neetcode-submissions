class MinStack:

    def __init__(self):
        # Initialize two stacks - original list and one to track minimum value
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        elif value < self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            # top of min_stack if less than, so add it into stack again - tracking minimum value
            self.min_stack.append(self.min_stack[-1])

        
    def pop(self) -> None:
        # Remove top elements from stack
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        # Return the top of the stack (last element pushed to stack)
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Return the minimum value, which will always be on top of min_stack
        return self.min_stack[-1]
        
