class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        queue_sublist = deque()   # Keeps track of the indices

        for right in range(n):

            # Pop indices that are outside the current window
            if queue_sublist and queue_sublist[0] <= right - k:
                queue_sublist.popleft()

            # Pop smaller elements from the back
            while queue_sublist and nums[queue_sublist[-1]] < nums[right]:
                queue_sublist.pop()

            # Append current index
            queue_sublist.append(right)

            # Record the maximium
            if right >= k - 1:
                result.append(nums[queue_sublist[0]])

        return result