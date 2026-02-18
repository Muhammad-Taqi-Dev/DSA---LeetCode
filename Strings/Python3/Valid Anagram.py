class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for item in s:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

        for rel in t:
            if rel in freq:
                freq[rel] -=1

        for value in freq.values():
            if value != 0:
                return False

        return True