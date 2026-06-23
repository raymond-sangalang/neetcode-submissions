class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pointer from both ends
        front_ptr = 0
        back_ptr = len(s) - 1
        s = s.lower()

        if len(s) == 1:
            return True

        # Iterate pointers inward comparing their alphanumeric values
        while front_ptr < back_ptr:
           
            # Check if front element is a letter
            if not s[front_ptr].isalnum():
                front_ptr += 1
                continue
            # Check if back element is a letter
            if not s[back_ptr].isalnum():
                back_ptr -= 1
                continue

            # Compare both elements
            if s[front_ptr] != s[back_ptr]:
                return False

            front_ptr += 1
            back_ptr -= 1
            
        return True