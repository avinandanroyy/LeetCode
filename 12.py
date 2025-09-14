class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = []
        
        for i in range(len(values)):
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]
        
        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3))      # "III"
    print(sol.intToRoman(58))     # "LVIII"
    print(sol.intToRoman(1994))   # "MCMXCIV"
