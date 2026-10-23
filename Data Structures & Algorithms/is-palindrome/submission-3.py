class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = []
        for c in s:
            char = c.lower()
            if ord('0') <= ord(char) <= ord('9') or ord('a') <= ord(char) <= ord('z'):
                palindrome.append(char)

        return palindrome == palindrome[::-1]