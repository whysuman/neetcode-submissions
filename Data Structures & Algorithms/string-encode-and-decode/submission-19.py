class Solution:

    def encode(self, strs: List[str]) -> str: 
        print(f"The input is : {strs}")       
        encoded_str = ""
        for string in strs:
            encoded_str += f"{len(string)}$"
            encoded_str += string
        print(f"The encoded string is :{encoded_str}") 
        return encoded_str


    def decode(self, s: str) -> List[str]:        
        final_list = []
        curr_str = ""
        number = 0
        for idx,char in enumerate(s):
            print(f"The current char is :{char}")
            
            if char == "$" and number == 0:
                if curr_str == "0":
                    final_list.append("")
                    continue
                
                number = int(curr_str)
                curr_str = ""
                continue

            if number > 0:
                curr_str+=char
                number-=1
                if number == 0:
                    final_list.append(curr_str)
                    print(f"String to be added in the final str: '{curr_str}'")
                    curr_str = ""
                continue    
            
            curr_str+=char
        
        return final_list