class Solution:
    def letterCombinations(self, digits: str):
        res = []
        if not digits:
            return res

        digitToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(''.join(comb))
                return

            letters = digitToLetters[digits[idx]]
            for letter in letters:
                comb.append(letter)
                backtrack(idx + 1, comb)
                comb.pop()

        backtrack(0, [])
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations("2"))
