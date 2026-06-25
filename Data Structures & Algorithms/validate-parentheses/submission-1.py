class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in brackets_dict.keys() and stack and stack[-1] == brackets_dict[ch]: 
                stack.pop()
            else:
                stack.append(ch)
          
        return len(stack) == 0