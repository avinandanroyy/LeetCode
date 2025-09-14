class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        max_val = float('-inf')
        for d1 in range(10):
            for d2 in range(10):
                if str(d1) in num_str:
                    new_num = num_str.replace(str(d1), str(d2))
                    max_val = max(max_val, int(new_num))
        
        min_val = float('inf')
        for d1 in range(10):
            for d2 in range(10):
                if str(d1) in num_str:
                    new_num = num_str.replace(str(d1), str(d2))
                    min_val = min(min_val, int(new_num))
        
        return max_val - min_val
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.minMaxDifference(11891))
    print(sol.minMaxDifference(90))