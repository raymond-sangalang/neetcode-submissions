from collections import defaultdict

class Solution:

    """
    1 - 1
    2 - 2
    3 - 3

    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_freq = defaultdict(int)
        num_set = set()                    # holds numbers already read
        freq_listNums = defaultdict(list)

        for num in nums:
            count_freq[num] += 1

            if num not in num_set:
                num_set.add(num)
                freq_listNums[1].append(num)
            
            else:
                # num is already contained
                # add into new location
                freq_listNums[count_freq[num]].append(num)

                # remove from previous location
                freq_listNums[count_freq[num] - 1].remove(num)


        merge_list = []
        for sub_list in freq_listNums.values():
            merge_list.extend(sub_list)
        
        return merge_list[-k:]







        