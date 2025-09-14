class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        result = 0
        sign = 1

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Check for optional '+' or '-' sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = 1 if s[i] == '+' else -1
            i += 1

        # Process numerical digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result

if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))               # Output: 42
    print(sol.myAtoi("   -42"))           # Output: -42
    print(sol.myAtoi("4193 with words"))  # Output: 4193
    print(sol.myAtoi("words and 987"))    # Output: 0
    print(sol.myAtoi("-91283472332"))     # Output: -2147483648 (INT_MIN)
