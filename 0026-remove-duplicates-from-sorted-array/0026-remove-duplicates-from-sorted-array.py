class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        k=1
        for r in range(len(nums)):
            if nums[r]!=nums[l]:
                l+=1
                nums[l]=nums[r]
                k+=1
        return k