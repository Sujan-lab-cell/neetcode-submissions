class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for n in range(len(nums)):
            diff=target-nums[n]
            if diff in seen:
                return [seen[diff],n]
            else:
                seen[nums[n]]=n