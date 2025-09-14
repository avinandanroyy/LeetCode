from collections import Counter
from itertools import accumulate
from math import inf

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())
        n = len(freq)
        dels = 0
        lowestDels = inf
        j = 0
        pl = list(accumulate(freq[i] for i in range(n - 1, -1, -1)))[::-1] + [0]

        for i in range(n):
            while j < n and freq[j] <= freq[i] + k:
                j += 1

            d = dels + pl[j] - (n - j) * (freq[i] + k)

            if d < lowestDels:
                lowestDels = d

            dels += freq[i]

        return lowestDels
    
if __name__ == "__main__":
    sol = Solution()

    word = "aabcaba"
    k = 0
    hell = "dabdcbdcdcd"
    x = 2
    blade = "aaabaaa"
    y = 2

    print(sol.minimumDeletions(word,k))
    print(sol.minimumDeletions(hell,x))
    print(sol.minimumDeletions(blade,y))