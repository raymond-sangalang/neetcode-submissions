class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        lengthNum1, lengthNum2 = len(nums1), len(nums2)
        
        # A has smaller amount of elements
        A, B = (nums1, nums2) if lengthNum1 < lengthNum2 else (nums2, nums1)
        lengthA, lengthB = len(A), len(B)
       
        total = lengthNum1 + lengthNum2
        mid = total // 2
        left, right = 0, lengthA - 1
        
        while True:
            
            a_index = (left + right) // 2  # A pointer
            b_index = mid - a_index - 2  # B pointer
            
            Aleft = A[a_index] if a_index >= 0 else float("-inf")
            Aright = A[a_index + 1] if (a_index + 1) < lengthA else float("inf")
            
            Bleft = B[b_index] if b_index >= 0 else float("-inf")
            Bright = B[b_index + 1] if (b_index + 1) < lengthB else float("inf")

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