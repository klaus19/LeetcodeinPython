from typing import List


def mergeSortedArrays(A: List[int], B: List[int]) -> List[int]:

    res = [*A,*B]
    return sorted(res)


class Solution:
    pass


if __name__ == "__main__":
    pt = [1, 2, 3, 4, 4]
    tp = [2, 4, 5, 5]
    print(mergeSortedArrays(pt, tp))
