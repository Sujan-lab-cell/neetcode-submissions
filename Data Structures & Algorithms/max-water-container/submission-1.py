class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxvol=0
        while l<r:
            width=r-l
            minhig=min(heights[l],heights[r])
            curvol=width*minhig
            maxvol=max(maxvol,curvol)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxvol
            

        