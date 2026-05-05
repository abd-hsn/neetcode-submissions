class Solution:

    def encode(self, strs: List[str]) -> str:
        my_encoded = ""
        if strs == []:
            return my_encoded
        split_token = "[SPLIT]"
        my_encoded = my_encoded +split_token
        for i,s in enumerate(strs):
            my_encoded = my_encoded +s
            if i==len(strs)-1:
               break
            my_encoded = my_encoded +split_token
            
        return my_encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        split_token = "[SPLIT]"
        splitted = s.split(split_token)
        strs = []
        for s in splitted:
            strs.append(s)
        return strs[1:]