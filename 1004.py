class Solution:
    def longestOnes(self, nums, k):
        left = 0
        max_len = 0
        zeros = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len

if __name__ == "__main__":
    sol = Solution()

    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    x = 3

    print(sol.longestOnes(nums,k))
    print(sol.longestOnes(arr,x))