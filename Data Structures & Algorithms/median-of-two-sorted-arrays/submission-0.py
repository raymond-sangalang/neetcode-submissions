class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # A has smaller amount of elements
        A, B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
       
        total = len(nums1) + len(nums2)
        mid = total // 2
        left, right = 0, len(A) - 1
        
        while True:
            
            a_index = (left + right) // 2  # A pointer
            b_index = mid - a_index - 2  # B pointer
            
            Aleft = A[a_index] if a_index >= 0 else float("-inf")
            Aright = A[a_index + 1] if (a_index + 1) < len(A) else float("inf")
            
            Bleft = B[b_index] if b_index >= 0 else float("-inf")
            Bright = B[b_index + 1] if (b_index + 1) < len(B) else float("inf")

            # cond: partition of arrays are ordered
            if Aleft <= Bright and Bleft <= Aright:
                
                if total % 2:                   # odd number of elements
                    return min(Aright, Bright)
                # even number of elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                right = a_index - 1
                
            else:
                left = a_index + 1