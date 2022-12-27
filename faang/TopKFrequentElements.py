from collections import Counter
from typing import List


class Solution(object):

    def top_k_frequent(self, k, nums):
        # Step 1: Create a dictionary to store the frequency of each element

        frequency = Counter(nums)

        # Step 2: Sort the dictionary by value in descending order

        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        # step 3: Return the top k elements from the sorted dictionary

        return [x[0] for x in sorted_frequency[:k]]


if __name__ == "__main__":
    pt = [1, 1, 1, 2, 2, 3, 4]
    k = 2
    print(Solution().top_k_frequent(k, pt))
