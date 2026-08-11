class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        
        sorted_store = dict(sorted(store.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_store.keys())[:k]