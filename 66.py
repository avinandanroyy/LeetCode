from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            
            i += 1
        return digits[::-1]

if __name__ == "__main__":
    sol = Solution()

    #Example 1
    digits = [1,2,3]
    print(sol.plusOne(digits))

    #Example 2
    digits1 = [4,3,2,1]
    print(sol.plusOne(digits1))

    #Example 3
    digits2 = [9]
    print(sol.plusOne(digits2))
