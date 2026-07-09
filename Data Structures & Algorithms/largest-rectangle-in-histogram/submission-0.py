class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][0]:
                h, _wi = stack.pop()
                w = index - _wi
                max_area = max(max_area, h*w)
                start = _wi
            # insert tuples of height with their corresponding index
            stack.append((height, start))  

        while stack:
            h, _wi = stack.pop()
            w = n - _wi
            max_area = max(max_area, h*w)

        return max_area

    """
    # Time Complexity: O(n)
    # Space complexity: O(n)
    ex1)
    [2,1,5,6,2,3]
    stack
    ______
    [(2, 0)]
    [(1, 0), (5, 2), (6, 3)]
    [(1, 0), (5, 2)]

    - extending with higher heights onto the stack
    - when reaching a lower height, it is then cut off b/c cannot for rectangle

    Area = Height * Width

    """