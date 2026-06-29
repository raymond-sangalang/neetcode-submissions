class Solution:
    """
    track difference from max heights on left and right ends
    with respect to their left and right pointers current heights

    max_left = 0
    max_right = 1
     
    [0 1 0 2 1 0 1 3 2 1 2 1]
       >                   <     mL: 1, mR: 1, rv: 0
       >                 <       mL: 1, mR: 2, rv: 0
         >               <       mL: 1, mR: 2, rv: 0 + (1-0)
           >             <       mL: 2, mR: 2, rv: 1 + (2-2)
           >           <         mL: 2, mR: 2, rv: 1 + (2-1)
           >         <           mL: 2, mR: 2, rv: 2 + (2-2)
           >       <             mL: 2, mR: 3, rv: 2 + (3-3)
             >     <             mL: 2, mR: 3, rv: 2 + (2-1)
               >   <             mL: 2, mR: 3, rv: 3 + (2-0)
                 > <             mL: 2, mR: 3, rv: 5 + (2-1) 
                                 end (left >= right)          rv: 6
    """
    def trap(self, height: List[int]) -> int:
         
        left = 0
        right = len(height) - 1
        left_max = height[left]    # tracks maximum left pointer height so far
        right_max = height[right]  # tracks maximum right pointer height so far
        rv = 0        # return value (area of trapped water)

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                rv += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                rv += right_max - height[right]
        return rv