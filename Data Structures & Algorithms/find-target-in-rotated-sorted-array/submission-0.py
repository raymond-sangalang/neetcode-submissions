class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[right]:    # right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:                           # left side is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid 
                else:
                    left = mid + 1
        return left if nums[left] == target else -1