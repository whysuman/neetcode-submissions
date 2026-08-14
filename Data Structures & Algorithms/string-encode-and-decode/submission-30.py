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
        count = 0
        num = ""
        for index in range(len(s)):
            char = s[index]
            if char == "#" and count == 0:
                count = int(num)
                if count == 0:
                    result.append("")
                    continue
                
                print(f"num: {num}")
                print(f"count:{count}")
                start = index + 1
                end = start + count 
                print(f"start: {start}, end: {end}")
                word = s[start:end]
                result.append(word)
                
                num = ""
            else:
                if count == 0:
                    num+=char
                    continue
                count-=1
                continue
            print(index,count)
                
        return result
