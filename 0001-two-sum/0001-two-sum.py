class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for ind,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return [seen[diff],ind]
            seen[num]=ind
            
        