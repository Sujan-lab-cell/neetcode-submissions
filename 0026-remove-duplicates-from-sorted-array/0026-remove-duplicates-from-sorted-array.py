class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s,f=0,1
        if len(nums)==0:
            return 0
        while f<len(nums) and s<f:
            if nums[s]==nums[f]:
                f+=1
            else:
                s+=1
                nums[s]=nums[f]
                f+=1
        return s+1



        