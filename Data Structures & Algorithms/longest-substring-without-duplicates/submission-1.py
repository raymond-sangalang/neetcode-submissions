class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()  # tracks characters visited in the window
        max_substr = 0

        left = 0         # tracks left boundary of the current window

        # Each iteration expands the window by 
        #  including strings index pointed to by right
        for right in range(len(s)):
            # Shrinks the window size by removing duplicate 'visited' character
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
              
            visited.add(s[right])
            max_substr = max(max_substr, right - left + 1)   

        return max_substr