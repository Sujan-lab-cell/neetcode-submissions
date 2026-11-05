class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for n in t:
            freq[n]=freq.get(n,0)-1
        
        if all(values==0 for values in freq.values()):
            return True
        else:
            return False