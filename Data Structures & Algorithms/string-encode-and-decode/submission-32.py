class Solution:

    def encode(self, strs: List[str]) -> str:
        #input string = ["Imagine", "#life","getting","better"]
        words = []
        for string in strs:
            string = f"{str(len(string))}#{string}"
            words.append(string)
        
        result = "".join(words)
        print(result)

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        count = 0
        num = ""
        while index < len(s):
            while s[index] != '#':
                num+=s[index]
                index+=1
            if s[index] == "#":
                count = int(num)
                if count == 0:
                    result.append("")
                    num = ""
                    index +=1
                    continue

                start = index + 1
                end = start + count
                result.append(s[start:end])
                index = end
                num = ""
                print(index)
                
        return result
