class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestDiff = float('inf')
        n = len(nums)
        
        for i in range(n):
            if closestDiff == 0:
                break
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                currDiff = target - total
                
                if abs(currDiff) < abs(closestDiff):
                    closestDiff = currDiff
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return target - closestDiff

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
    print(sol.threeSumClosest([0,0,0],1)) #Output: 0
