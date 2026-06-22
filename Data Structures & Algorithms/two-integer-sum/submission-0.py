class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index in range(len(nums)):
            num_to_target = target - nums[index]

            if num_to_target not in nums[index+1:]:
                continue
           
            return [index, nums[index+1:].index(num_to_target)+index+1]
        