class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        result = []
        found = False

        for word in strs:
            found = False
            letters = {}
            for c in word:
                letters[c] = 1 + letters.get(c, 0)
            for i, anagram in enumerate(anagrams):
                if letters == anagram:
                    result[i].append(word)
                    found = True
                    break
            if not found:
                result.append([word])
                anagrams.append(letters)
        return result