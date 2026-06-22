from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict = defaultdict(int)

        n = len(s)
        m = len(t)
        if m != n:
            return False
        
        for index in range(n):
            letter_dict[s[index]] += 1
            letter_dict[t[index]] -= 1
        
        for count in letter_dict.values():
            if count != 0:
                return False
        
        return True

        