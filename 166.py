from typing import List

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
    
        num, den = abs(numerator), abs(denominator)

        result.append(str(num // den))
        remainder = num % den

        if remainder == 0:
            return "".join(result)

        result.append(".")
    
        remainders_map = {remainder: len(result)} 

        while remainder != 0:
            remainder *= 10
        
            result.append(str(remainder // den))
        
            remainder %= den

            if remainder in remainders_map:
                start_index = remainders_map[remainder]
            
                result.insert(start_index, "(")
            
                result.append(")")
            
                break
        
            remainders_map[remainder] = len(result)

        return "".join(result)
sol = Solution()

print(sol.fractionToDecimal(1,2))
print(sol.fractionToDecimal(2,1))
print(sol.fractionToDecimal(4,333))