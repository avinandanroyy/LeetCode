class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revs1 = version1.split('.')
        revs2 = version2.split('.')
    
        n1, n2 = len(revs1), len(revs2)
        max_len = max(n1, n2)
    

        for i in range(max_len):
            rev1_val = int(revs1[i]) if i < n1 else 0
            rev2_val = int(revs2[i]) if i < n2 else 0

            if rev1_val > rev2_val:
                return 1
            elif rev1_val < rev2_val:
                return -1
            

        return 0

sol = Solution()
version1 = "1.2"
version2 = "1.10"
print(sol.compareVersion(version1,version2))