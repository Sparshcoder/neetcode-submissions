from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold the groups: key = sorted string, value = list of anagrams
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort the string to create a uniform key for all anagrams (e.g., "eat" -> "aet")
            sorted_s = "".join(sorted(s))
            anagram_map[sorted_s].append(s)

        # Return all the grouped lists
        return list(anagram_map.values())
