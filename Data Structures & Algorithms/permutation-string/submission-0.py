from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        substr_dict = defaultdict(int)
        compare_freq = defaultdict(int)

        for i in range(n1):
            substr_dict[s1[i]] += 1
            compare_freq[s2[i]] += 1

        if substr_dict == compare_freq:
            return True

        for i in range(n1, n2):
            left_char = s2[i - n1]
            compare_freq[left_char] -= 1
            if compare_freq[left_char] == 0:
                del compare_freq[left_char]

            compare_freq[s2[i]] += 1

            if substr_dict == compare_freq:
                return True

        return False