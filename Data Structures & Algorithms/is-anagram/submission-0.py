class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = self.create_hashmap(s)
        t_chars = self.create_hashmap(t)

        # Check that character frequency matches
        for char in s_chars:
            if char not in t_chars:
                return False
                
            if s_chars[char] != t_chars[char]:
                return False

        return True

    def create_hashmap(self, string):
        hashmap = {}
        for char in string:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        return hashmap
