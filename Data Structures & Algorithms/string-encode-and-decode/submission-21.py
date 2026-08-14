class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for string in strs:
            final_str += f"{len(string)}$" + string
        print(f"Encoded String: {final_str}")
        return final_str

# 0$4$neet4$code4$love3$you
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j +=1 
            length = int(s[i:j])
            print(f"Length of the current string: {length}")
            i = j + 1
            j += length + 1
            print(f"The current string is {s[i:j]}")
            result.append(s[i:j])
            i = j

        return result