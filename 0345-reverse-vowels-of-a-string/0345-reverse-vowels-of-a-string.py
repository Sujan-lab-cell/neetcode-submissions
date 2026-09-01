class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r=0,len(s)-1
        s=list(s)
        for _ in range(len(s)):
            if l>r:
                break
            if s[l] not in "aeiouAEIOU":
                l+=1
                continue
            if s[r] not in "aeiouAEIOU":
                r-=1
                continue
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)
        