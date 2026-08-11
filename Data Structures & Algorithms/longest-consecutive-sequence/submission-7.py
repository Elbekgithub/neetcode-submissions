class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in distinct_nums:
                
                count = 1
                while num + count in distinct_nums:
                    count += 1
                
                longest = max(longest, count)
            
        return longest


