class Solution:
    def is_anagram(self,word1,word2):
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        if len(word1) != len(word2):
            return False
        l=len(word1) 
        c=[0]*26
        for i in range(l):
            c[ord(word1[i]) - ord('a')] +=1
            c[ord(word2[i]) - ord('a')] -=1
        for j in c:
            if j!=0:
                return False
        return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        grouped_anagrams[strs[0]]=[strs[0]]
        for word in strs[1:]:
            anagram_found = False
            for key in grouped_anagrams.keys():
                anagram_found = self.is_anagram(word,key)                
                if anagram_found:
                    grouped_anagrams[key].append(word)
                    break
            
            if not anagram_found:
                grouped_anagrams[word]=[word]
        
        return [ group for group in grouped_anagrams.values()]


        