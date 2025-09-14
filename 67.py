
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a,2), int(b,2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry

        return bin(a)[2:]
    
if __name__ == "__main__":
    a = "11"
    b = "1"
    c = "1010"
    d = "1011"

    sol = Solution()
    print(sol.addBinary(a, b))
    print(sol.addBinary(c,d))