class Solution(object):

    def secondLargest(self,arr):

        max_no = float('-inf')
        min_no = float('-inf')

        for num in arr:
            if num > max_no:
                max_no = num
                min_no = max_no
            elif num > min_no and num!=max_no:
                min_no = num
        return min_no