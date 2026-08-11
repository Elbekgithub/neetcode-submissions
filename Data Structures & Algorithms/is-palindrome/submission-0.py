class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        i, r = 0, len(s)-1
        while i < r:
            if s[i] != s[r]:
                return False
            i += 1
            r -= 1
        return True