class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        check = strs[0]
        for i in range(len(check)):
            for word in strs[1:]:
                
                if i == len(word) or check[i] != word[i]:
                    return check[:i]

        return check