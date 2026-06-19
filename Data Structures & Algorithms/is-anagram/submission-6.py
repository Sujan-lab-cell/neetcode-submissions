from collections import Counter,defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        freq=defaultdict(set)
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            if ch not in freq:
                return False
            freq[ch]-=1
            if freq[ch]<0:
                return False
        return True
        