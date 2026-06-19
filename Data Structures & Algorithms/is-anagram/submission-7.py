class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count=[0]*26
        for ch in s:
            count[ord(ch)-ord("a")]+=1
        for ch in t:
            count[ord(ch)-ord("a")]-=1
        return all(x==0 for x in count)
        # for x in count:
        #     if x!=0:
        #         return False
        # return True
        