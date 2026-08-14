class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        
        print(f"""Original String S: {s} and Sorted String: {sorted_s}
Original String T: {t} and its sorted string T: {sorted_t}""")
        if sorted_s == sorted_t:
            return True
        else:
            return False
        