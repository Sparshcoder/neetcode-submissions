from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        counter_dict = {x:0 for x in nums_set}
        for i in nums:
            if i in counter_dict:
                counter_dict[i] = counter_dict.get(i)+1
        
        # 2. Sort the dictionary items by their frequency (values) in descending order
        sorted_items = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)

        # 3. Grab the top k keys cleanly, stopping once we hit k elements
        final_list = []
        for key, value in sorted_items:
            final_list.append(key)
            if len(final_list) == k:
                break

        return final_list

        
