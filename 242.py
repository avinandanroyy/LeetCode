from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
    
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    x = "rat"
    y = "car"

    sol = Solution()

    print(sol.isAnagram(s,t))
    print(sol.isAnagram(x,y))