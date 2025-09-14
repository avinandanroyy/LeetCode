from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currentSum = 0
        prefixSums = {0 : 1}

        for n in nums:
            currentSum += n
            difference = currentSum - k

            result += prefixSums.get(difference,0)
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum,0)

        return result
    
if __name__ == "__main__":
    sol = Solution()

    nums = [1,1,1]
    k = 2
    arr = [1,2,3]
    x = 3

    print(sol.subarraySum(nums,k)) #Wrong Answer. Output = 1 Expected = 2
    print(sol.subarraySum(arr,x))  #Wrong Answer. Output = 1 Expected = 2


   