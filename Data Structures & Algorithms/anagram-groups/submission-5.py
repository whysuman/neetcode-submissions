class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for string in strs:
            char_map = [0]*26
            for char in string:
                char_map[ord(char) - ord('a')]+=1
            
            mapping[tuple(char_map)].append(string)
        
        final_res = []
        for keys,val in mapping.items():
            print(val)
            final_res.append(val)

        print(final_res)
        return final_res
                

