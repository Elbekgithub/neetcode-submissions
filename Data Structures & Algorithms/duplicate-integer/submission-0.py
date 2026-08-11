class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counter = {}
        for num in nums:
            if num in num_counter:
                return True
            else:
                num_counter[num]=1
        return False 