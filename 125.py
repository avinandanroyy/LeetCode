class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        for i in s:
            if i.isalnum():
                temp = temp + i
        return temp == temp[::-1]
        
if __name__ == "__main__":
    sol = Solution()

    s = "A man, a plan, a canal: Panama"
    u = "race a car"
    t = " "

    print(sol.isPalindrome(s))
    print(sol.isPalindrome(u))
    print(sol.isPalindrome(t))