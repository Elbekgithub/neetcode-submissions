class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i, num in enumerate(nums):
            num_j = target-num
            if num_j in nums[i+1: l]:
                return [i, nums.index(num_j, i+1)]
        return 
                