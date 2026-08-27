class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,1
        k=1
        while r<len(nums):
            if nums[l]==nums[r]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
                k+=1
                r+=1
        return k