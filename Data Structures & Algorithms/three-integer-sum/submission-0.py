class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_set= set()
        N= len(nums)
        nums= sorted(nums)
        for index in range(N-2):
            
            if index == 0 or nums[index] > nums[index-1]:
                front= index+1
                back= N-1
                ''' runs to check element with all double combinations at end of list'''
                """ permutation n choose r:  -(nums[i-1]+nums[count]) == 0   """
                while front < back:
  
                    value = nums[index]+nums[front]+nums[back]
                    if value == 0:
                        list_set.add((nums[index],nums[front],nums[back]))
                    if value < 0:
                        start_index= front
                        
                        while nums[front]==nums[start_index] and front < back:
                            front += 1
                    else:
                        end_index= back
                        
                        while nums[back]==nums[end_index] and front < back:
                            back -= 1
        return list(list_set)