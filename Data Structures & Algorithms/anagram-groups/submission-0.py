from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            words_dict[sorted_word].append(word)
        return list(words_dict.values())