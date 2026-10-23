class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += word + ":;"
        return result
    def decode(self, s: str) -> List[str]:
        result = s.split(":;")
        return result[:len(result)-1]