class Solution:
    def isValid(self, s: str) -> bool:
        

        closeBrkts = {")" : "(","]" : "[", "}" : "{"}
        curr = []
        for indx,bracket in enumerate(s):
            if bracket in closeBrkts:
                if curr == []:
                    return False
                currentbr = curr.pop()

                if closeBrkts[bracket] != currentbr:
                    return False
            else:
                curr.append(bracket)

        if curr != []:
            return False

        return True