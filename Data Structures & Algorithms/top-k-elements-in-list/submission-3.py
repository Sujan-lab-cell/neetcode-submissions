class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        mk=[num for num,cnt in Counter(nums).most_common(k)]
        return mk
        