class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counter = set()
        for num in nums:
            if num in num_counter:
                return True
            else:
                num_counter.add(num)
        return False 