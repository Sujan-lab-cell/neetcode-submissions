class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total=sum(nums[:k])
        max_total=total

        for i in range(k,len(nums)):
            total-=nums[i-k]
            total+=nums[i]

            max_total=max(max_total,total)
        return max_total/k      