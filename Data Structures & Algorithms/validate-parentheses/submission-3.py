class Solution:
    def isValid(self, s: str) -> bool:
        lifos = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for indx,char in enumerate(s):
            # ([{}()][])
            print(char)
            if char in closeToOpen:
                if lifos and lifos[-1] == closeToOpen[char]:
                    last = lifos.pop()
                else:
                    return False
            else:
                lifos.append(char)
            # print(last)

        if lifos != []:
            return False
        else:
            return True