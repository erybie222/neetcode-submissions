class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 1
        result = []
        while i < len(s):
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            start = j+1
            result.append(s[start:start+length])
            i = start + length
            j = i + 1
        return result