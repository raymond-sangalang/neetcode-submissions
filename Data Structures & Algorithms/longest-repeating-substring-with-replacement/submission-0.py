class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hmap = {}          # counts freq of characters
        left = right = 0   # sides/boundaries of the window
        longest = 0
        max_freq = 0
    
        while right < len(s):
            hmap[s[right]] = hmap.get(s[right], 0) + 1
            max_freq = max(max_freq, hmap[s[right]])

            # Number of replacements, k is greater than
            # the number of replacement allowed, therefore we shift
            # the left boundary
            while (right - left + 1) - max_freq > k:
                hmap[s[left]] -= 1
                if hmap[s[left]] == 0:
                    hmap.pop(s[left])
                left += 1   # move the left boundary

            # Updating the return value
            longest = max(longest, right - left + 1)
            right += 1

        return longest