class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        N = len(nums)
        num_set = set()
        for i in range(N):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        return False
        