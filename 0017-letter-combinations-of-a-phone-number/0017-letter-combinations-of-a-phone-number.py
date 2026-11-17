
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(index, s):
            if index == len(digits):
                res.append(s)
                return

            letters = mp[digits[index]]

            for ch in letters:
                backtrack(index + 1, s + ch)

        backtrack(0, "")
        return res
