from collections import Counter


class Solution(object):
    def mostFrequentEven(self, nums):
        num_dict = Counter(nums)
        n = len(nums)

        most_frequent_even = None
        max_count=0

        for num,count in num_dict.items():
            if num % 2 ==0:
                if count > max_count:
                    most_frequent_even= num
                    max_count=count
        return most_frequent_even

if __name__ == '__main__':
    nums = [2, 2, 2, 3, 3, 4, 4, 4, 4]
    result = Solution().mostFrequentEven(nums)
    print(result)








