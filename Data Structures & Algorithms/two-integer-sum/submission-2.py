class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        pairs = {}
        for i, num in enumerate(nums):
            num_j = target-num
            if num_j in pairs:
                return [pairs[num_j], i]
            else:
                pairs[num] = i
        return []