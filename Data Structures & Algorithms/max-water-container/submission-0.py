class Solution:
    def maxArea(self, heights: List[int]) -> int:

        rv_maxArea = 0                        # track the largest area
        start, end = 0, len(heights) - 1      # initialize start and end pointers

        # Adjust pointers accordingly by their heights
        # and track the max area
        while start < end :
            rv_maxArea = max( rv_maxArea, (end-start) * min(heights[start], heights[end]) )
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return rv_maxArea