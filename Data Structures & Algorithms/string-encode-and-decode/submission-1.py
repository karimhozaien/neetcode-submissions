class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return None
        for word in range(len(strs)):
            string = "!".join(strs)
            print(string)
        return string

    def decode(self, s: str) -> List[str]:
        if s == None:
            return []
        string = s.split("!")
        print(string)
        return string
