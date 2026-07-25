class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trackingset = set()
        for i in nums:
            if i in trackingset:
                return True
            trackingset.add(i)
        return False