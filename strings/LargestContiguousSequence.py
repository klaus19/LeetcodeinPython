class Solution(object):

    def find_largest_contiguous_sequence(self, numbers):

        max_so_far = -1e8
        max_ending = 0

        for i in range(0, len(numbers)):
            max_ending = max_ending + numbers[i]

            if max_so_far < max_ending:
                max_so_far = max_ending

            if max_ending < 0:
                max_ending = 0
        return max_so_far


if __name__ == '__main__':
    pt = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(Solution().find_largest_contiguous_sequence(pt))
