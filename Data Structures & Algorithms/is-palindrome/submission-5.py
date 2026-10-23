class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        l, r = 0 , len(s) - 1

        while l < r:
            first,  last = s[l].lower(), s[r].lower()
            while not first.isalnum() and l < r:
                l += 1
                first = s[l].lower()
            while not last.isalnum() and l < r:
                r -= 1
                last = s[r].lower()
            if first != last:
                return False
            else:
                l += 1
                r -= 1
        return True
