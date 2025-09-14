class Solution:
    def kthCharacter(self, k: int) -> int:
        ans = 0
        while k > 1:
            l = k.bit_length() - 1  
            if (1 << l) == k:
                t = 1
            else:
                t = 1 << l
            k -= t
            ans += 1
        
        return chr(ord("a") + ans)
    
if __name__ == "__main__":
    k = 5
    sol = Solution()
    print(sol.kthCharacter(k))