class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for r in range(len(nums)):
            diff=target-nums[r]
            if diff in seen:
                return [r,seen[diff]]
            seen[nums[r]]=r
            
        