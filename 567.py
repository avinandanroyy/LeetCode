class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or len(s2) == 0:
            return False
        if len(s1) == 0:
            return True

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for c in s2[:len(s1)]:
            count2[ord(c) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(len(s1), len(s2)):
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            count2[ord(s2[i]) - ord('a')] += 1

            if count1 == count2:
                return True

        return False

sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))   # True
print(sol.checkInclusion("ab", "eidboaoo"))   # False
