class Solution:
    def nextGreaterElement(self, nums1, nums2):
        if not nums2 or not nums1:
            return []
        
        numberNGE = {}
        numStack = []
        
        numStack.append(nums2[-1])
        numberNGE[nums2[-1]] = -1
        
        for i in range(len(nums2) - 2, -1, -1):
            if nums2[i] < numStack[-1]:
                numberNGE[nums2[i]] = numStack[-1]
                numStack.append(nums2[i])
                continue

            while numStack and numStack[-1] < nums2[i]:
                numStack.pop()
            
            if not numStack:
                numberNGE[nums2[i]] = -1
                numStack.append(nums2[i])
            else:
                numberNGE[nums2[i]] = numStack[-1]
                numStack.append(nums2[i])
        
        return [numberNGE[num] for num in nums1]

sol = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(sol.nextGreaterElement(nums1, nums2))
# Output: [-1, 3, -1]
