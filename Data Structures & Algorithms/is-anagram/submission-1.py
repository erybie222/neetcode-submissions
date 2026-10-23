class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        let1, let2 = {}, {}

        for c in s:
            if c not in let1.keys():
                let1[c] = 1
            else:
                let1[c] += 1
        
        for c in t:
            if c not in let2.keys():
                let2[c] = 1
            else:
                let2[c] += 1
        
        
        return let1 == let2