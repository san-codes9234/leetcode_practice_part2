from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        return Counter(nums) == Counter(list(range(1, n)) + [n, n])
