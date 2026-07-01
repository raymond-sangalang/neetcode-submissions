class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        tup_car = [(position[index], speed[index]) for index in range(n)] 
        stack = []
        for pos, sp in sorted(tup_car, reverse=True):
            stack.append((target-pos)/sp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)