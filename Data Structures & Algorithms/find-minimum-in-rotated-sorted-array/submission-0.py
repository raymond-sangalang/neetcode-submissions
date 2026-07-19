class Solution:
    def findMin(self, nums: List[int]) -> int:
    	n = len(nums)
    	if n == 1:
    		return nums[0]

    	left, right = 0, n-1       
 
    	while left < right:
    		mid = left + (right - left) // 2
    		# compare nums[mid] and nums[right] and update left or right
    		if nums[mid] > nums[right]:
    			left = mid+1
    		else:
    			right = mid

    	return nums[left]