
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_val = sum(nums[:k])
        best = max_val

        for right in range(k, len(nums)):
            max_val += nums[right] - nums[right - k]
            best = max(best, max_val)

        return best / k



        