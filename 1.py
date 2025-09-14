from typing import List

#This is Clasa
class TwoSum:

    #This is function
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []

#This is Main Method
if __name__ == "__main__":
    sol = TwoSum()

    #Example1
    nums1 = [2,7,11,15]
    target1 = 9
    print(sol.twoSum(nums1,target1))

    #Example2
    nums2 = [3,2,4]
    target2 = 6
    print(sol.twoSum(nums2,target2))