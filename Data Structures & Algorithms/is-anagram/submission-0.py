class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = list(s)
        letters2 = list(t)
     
        letters1.sort()
        letters2.sort()

        return (letters1 == letters2)