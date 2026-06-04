class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        frd=[]
        prd=1
        for i in nums:
            prd*=i
            frd.append(prd)
        back=[]
        prd=1
        for i  in nums[::-1]:
            prd*=i
            back.append(prd)
        back=back[::-1]
        op=[back[1]]
        for i in range(1,len(nums)-1):
            op.append(frd[i-1]*back[i+1])
        op.append(frd[-2])
        return op
                