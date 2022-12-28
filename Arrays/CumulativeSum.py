from typing import List

import numpy as np


class Solution:
    def getCumulativeSum(self, arr: List[int]) -> List[int]:
        sum = 0
        new_arr = []
        for i in arr:
            sum +=i
            new_arr.append(sum)
        return new_arr

    def secondary_method(self,arr):
        cumulative_sum=np.cumsum(arr)
        return cumulative_sum

    def third_method(self,arr):
        n = len(arr)
        cumulativeSum = [arr[0]] * n
        for i in range(1, n):
            cumulativeSum[i] = cumulativeSum[i - 1] + arr[i]
        return cumulativeSum


if __name__ == "__main__":
    pt = [1, 2, 3, 4]
    print(Solution().third_method(pt))
    # print(Solution().getCumulativeSum(pt))
    # print(Solution().secondary_method(pt))
