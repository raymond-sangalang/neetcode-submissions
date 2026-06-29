class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        r_array = [0] * n
        stack = []

        for i in range(n):
            # check the top of the stack to see if prior appended temperature
            # is less than the current temperature
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                _, j = stack.pop()
                r_array[j] = i - j
            stack.append((temperatures[i], i))
        return r_array
        