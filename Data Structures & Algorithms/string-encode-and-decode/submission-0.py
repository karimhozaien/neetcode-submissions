class Solution:

    def encode(self, strs: List[str]) -> str:
        for word in range(len(strs)):
            string = "!".join(strs)
            print(string)
        return string

    def decode(self, s: str) -> List[str]:
        string = s.split("!")
        print(string)
        return string
