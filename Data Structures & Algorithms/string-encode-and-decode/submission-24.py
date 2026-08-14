class Solution:

    def encode(self, strs: List[str]) -> str:
        encodee = ""
        for string in strs:
            curr_len = len(string)
            encodee += f"{curr_len}#" + string
        
        print(encodee)
        return encodee


    def decode(self, s: str) -> List[str]:
        
        length = 0
        final_res = []
        curr = ""
        for char in s:
            if char == "#" and length == 0:
                length = int(curr)
                if length == 0:
                    final_res.append("")
                curr = ""
                continue
            curr += char
            if length != 0:
                length -=1
                if length == 0:
                    final_res.append(curr)
                    print(f"Curr: {curr} and final: {final_res}")
                    curr = ""

        return final_res
            
                
            
            
                


        