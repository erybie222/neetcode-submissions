class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string = ""
        for char in s:
            if char.isalnum():
                alnum_string += char.lower()
        return (alnum_string == alnum_string[::-1])