class Solution(object):

    def get_second_largest(self,arr):
        second_max = float("-inf")

        max = float("-inf")

        for i in range(0, len(arr)):
            item = int(arr[i])
            if item > max:
             second_max = max
             max = item
            elif second_max < item < max:
             second_max = item

        return -1 if second_max == float("-inf") else second_max