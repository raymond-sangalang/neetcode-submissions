class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited_dict = dict()
        
        for index in range(len(nums)):
            num_to_target = target - nums[index]

            if num_to_target in visited_dict:
                return [visited_dict[num_to_target], index]

            visited_dict[nums[index]] = index