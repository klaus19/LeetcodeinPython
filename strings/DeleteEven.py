class Solution(object):
    def extract_odds(self, numbers):
        odd_numbers = []

        for i in range(0, len(numbers)):

            if numbers[i] % 2 == 0:
                pass
            else:
                odd_numbers.append(numbers[i])

        return odd_numbers


if __name__ == '__main__':
    pt = [1, 2, 3, 4, 5]
    print(Solution().extract_odds(pt))
