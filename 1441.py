from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_index = 0

        for i in range(1, n + 1):
            if target_index >= len(target):
                break
        
            if i == target[target_index]:
                operations.append("Push")
                target_index += 1
            else:
                operations.append("Push")
                operations.append("Pop")
        
        return operations

sol = Solution()

#Example 1
target1 = [1,3]
n1 = 3
print(sol.buildArray(target1,n1))
#Expected Output : ["Push","Push","Pop","Push"]

#Example 2
target2 = [1,2,3]
n2 = 3
print(sol.buildArray(target2,n2))
#Expected Output : ["Push","Push","Push"]

#Example 3
target3 = [1,2]
n3 = 4
print(sol.buildArray(target3,n3))
#Expected Output : ["Push","Push"]