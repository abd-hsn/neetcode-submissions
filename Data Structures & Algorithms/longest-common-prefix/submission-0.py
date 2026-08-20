class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # length_of_strings = [len(s) for s in strs]
        flag = [strs[0][:i+1] for i in range(len(strs[0]))]
        # flag = strs[0]
        prefix=""
        for f in flag:
            for word in strs:
                if not word.startswith(f):
                    return prefix
            prefix = f
        return prefix

        