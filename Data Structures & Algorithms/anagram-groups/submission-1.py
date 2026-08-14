class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_char = {}
        for ind,elem in enumerate(strs):
            char_count = [0] * 26
            for i,el in enumerate(elem):
                char_count[ord(elem[i]) - ord('a')]+=1

            if tuple(char_count) not in final_char:
                final_char[tuple(char_count)] = [elem]
            else:
                final_char[tuple(char_count)].append(elem)
        
        print(list(final_char.values()))
        return list(final_char.values()) 




























