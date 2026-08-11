from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for i in strs:
            store[tuple(sorted(i))].append(i)
        return list(store.values())
                