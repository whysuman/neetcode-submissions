class Solution:
    def isValid(self, s: str) -> bool:
        lifos = []

        for indx,char in enumerate(s):
            print(char)
            if char == '[' or char == '{' or char == "(":
                lifos.append(char)

            elif char == "]":
                if lifos != []:
                    last = lifos.pop()
                    if last != "[":
                        return False
                else:
                    return False
            
            elif char == "}":
                if lifos != []:
                    last = lifos.pop()
                    if last != "{":
                        return False
                else:
                    return False

            elif char == ")" :
                if lifos != []:
                    last = lifos.pop()
                    if last != "(":
                        return False
                else:
                    return False

            # print(last)

        if lifos != []:
            return False
        else:
            return True