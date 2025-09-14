class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
