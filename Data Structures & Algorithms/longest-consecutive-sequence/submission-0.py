class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        N = len(nums)
        if N == 0:
            return 0
        elif N == 1:
            return 1
        index = 1
        count = 1
        max_count = 1
      
        while index < N:
            if nums[index] == nums[index - 1]:
                index += 1
                continue

            if nums[index] == nums[index - 1] + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1

            index += 1

        return max(max_count, count)