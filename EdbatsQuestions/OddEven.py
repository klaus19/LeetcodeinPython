class Solution(object):

    def calculate_odd_even(self, li):
        even = 0
        odd = 0

        sum_num = []
        for x in li:
            if x % 2 == 0:
                even += x
            else:
                odd += x

        sum_num.append(even)
        sum_num.append(odd)
        return sum_num


if __name__ == "__main__":
    p = Solution()
    lit = [1, 2, 4, 5]
    print(p.calculate_odd_even(lit))
