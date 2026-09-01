class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums[:]=[x for x in nums if x!=0]+[0]*nums.count(0)