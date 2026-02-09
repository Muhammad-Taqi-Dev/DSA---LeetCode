class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            arr.append(i)
        for i in nums:
            arr.append(i)

        return arr