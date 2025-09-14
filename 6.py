class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ["" for _ in range(numRows)]
        cr = 0
        mod = 0
        dir = [1, -1]
        
        for ch in s:
            rows[cr] += ch
            newRow = cr + dir[mod]
            if newRow < 0 or newRow >= numRows:
                mod = (mod + 1) % 2
                newRow = cr + dir[mod]
            cr = newRow
        
        return "".join(rows)

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING",4))
