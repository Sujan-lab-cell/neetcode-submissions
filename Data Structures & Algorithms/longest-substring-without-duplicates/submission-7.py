class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        if len(s)==0:
            return 0
        l=0
        r=l
        seen=set()
        while r<len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l+=1
            else:
                seen.add(s[r])
                max_len=max(max_len,r-l+1)
                r+=1
        return max_len
        