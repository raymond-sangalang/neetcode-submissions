class Solution:
    def minWindow(self, s: str, t: str) -> str:

    	# Check if search string is empty
        if t == "":
        	return ""

        # Check if search will have enough elements to parse
        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return ""

        # Define the hashmaps to track the elements used in window
        dict_count, window = {}, {}

        # target characters and their frequencies to match in substring
        for ch in t:
        	dict_count[ch] = dict_count.get(ch, 0) + 1  

		# Define variables to keep track of the elements in the window
        have, need = 0, len(dict_count)                
        result, len_result = [-1, -1], float("inf")
        left = 0                                     # left boundary of the window
        for right in range(len_s):
        	ch = s[right]                            # current letter element
        	window[ch] = window.get(ch, 0) + 1       # book keeping of element frequency

        	# Check if current letter is within the target dictionary and 
        	# window substring contains count ch that matches the target frequency
        	if ch in dict_count and window[ch] == dict_count[ch]:
        		have += 1                             # update 'have' tracker

        	while have == need:
        		# update our result
        		if (right - left + 1)< len_result:
        			result = [left, right]
        			len_result = (right - left + 1)

        		# pop from the left of the window and update tracker when necessary
        		window[s[left]] -= 1
        		if s[left] in dict_count and window[s[left]] < dict_count[s[left]]:
        			have -= 1
        		# shift the left window boundary 
        		left += 1
        left, right = result

        return s[left:right+1] if len_result != float("inf") else ""