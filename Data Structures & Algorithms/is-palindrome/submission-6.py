class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s) - 1

        while l < r:
            first,  last = s[l], s[r]
            while not first.isalnum() and l < r:
                l += 1
                first = s[l]
            while not last.isalnum() and l < r:
                r -= 1
                last = s[r]
            if first.lower() != last.lower():
                return False
            else:
                l += 1
                r -= 1
        return True
