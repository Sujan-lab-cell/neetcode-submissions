class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        if len(heights)==0:
            return 0
        max_out=0
        while l<r:
            wid=r-l
            maxhi=min(heights[l],heights[r])
            vol=wid*maxhi
            max_out=max(vol,max_out)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_out
            

        