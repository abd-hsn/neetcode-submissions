class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)  != len(t):
            return False
            
        s = sorted(s)
        t = sorted(t)
        
        for sc in s:
            if sc not in t:
                return False
            else:
                t.remove(sc)
        return True
