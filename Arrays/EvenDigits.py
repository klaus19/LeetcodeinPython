from typing import List, Optional


class Solution:
    def getEvenDigitNumbers(self, arr: List[int]) ->\
            Optional[List[int]]:
        res = []
        for i in range(len(arr)):
            if len(str(arr[i]))%2 == 0:
                res.append(arr[i])
            else:
                pass
        return res


if __name__ == "__main__":
    pt = [42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442]
    print(Solution().getEvenDigitNumbers(pt))
