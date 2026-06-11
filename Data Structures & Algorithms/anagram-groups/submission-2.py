from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict=defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            dict[key].append(s)
        return list(dict.values())