from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic=defaultdict(list)
        for stre in strs:
            key=''.join(sorted(stre))
            dic[key].append(stre)
        return list(dic.values())
