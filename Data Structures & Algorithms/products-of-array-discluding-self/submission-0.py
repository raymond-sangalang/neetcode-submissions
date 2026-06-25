class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_size = len(nums)
        result = [1] * num_size               # create array and fill with all 1s
        left_side = right_side = 1            # variables to be product updated 
     
        # product of left side - insert first then update
        for index in range(num_size) :
            result[index] = left_side
            left_side *= nums[index]

        # iterate in reverse order, and mult prod of left with
        # product of right side,
        for index in range(num_size-1 , -1, -1):
            result[index] *= right_side
            right_side *= nums[index]
        
        return result