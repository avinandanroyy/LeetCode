from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n - 2):
            ai = arr[i]
            for j in range(i + 1, n - 1):
                aj = arr[j]
                if abs(ai - aj) > a:
                    continue
                for k in range(j + 1, n):
                    ak = arr[k]
                    diff_jk = abs(aj - ak)
                    if diff_jk > b:
                        continue
                    if abs(ai - ak) <= c:
                        count += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()

    arr, a , b , c = [3,0,1,1,9,7], 7, 2, 3
    arr1, x, y, z = [1,1,2,2,3], 0 , 0, 1

    print(sol.countGoodTriplets(arr,a,b,c))
    print(sol.countGoodTriplets(arr1,x,y,z))