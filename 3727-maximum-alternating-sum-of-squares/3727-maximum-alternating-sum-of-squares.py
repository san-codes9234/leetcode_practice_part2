class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        vals = sorted((abs(x) for x in nums), reverse=True)
        n = len(vals)
        pos_count = (n + 1) // 2 

        result = 0
        for i, v in enumerate(vals):
            if i < pos_count:
                result += v * v
            else:
                result -= v * v
        return result
