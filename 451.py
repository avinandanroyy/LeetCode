from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequencyMap = Counter(s)

        chars = sorted(frequencyMap.keys(), key=lambda c: frequencyMap[c], reverse=True)

        result = []
        for c in chars:
            result.append(c * frequencyMap[c])

        return ''.join(result)
    
sol = Solution()

print(sol.frequencySort("tree"))
print(sol.frequencySort("cccaaa"))
print(sol.frequencySort("Aabb"))
