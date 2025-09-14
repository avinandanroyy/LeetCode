from typing import List

class Solution:
    def valid(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0

        for num in pushed:
            stack.append(num)
            while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

        return pop_index == len(popped)

sol = Solution()

#Example 1
pushed1 = [1,2,3,4,5]
popped1 = [4,5,3,2,1]
print(sol.valid(pushed1,popped1))
#Expected Output : true

#Example 2
pushed2 = [1,2,3,4,5]
popped2 = [4,3,5,1,2]
print(sol.valid(pushed2,popped2))
#Expected Output. : false