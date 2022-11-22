class Solution(object):

    def discount_incurred(self, amount, percentage):
        discount = 0
        discount += amount * percentage / 100
        return discount


if __name__ == "__main__":
    p = Solution()
    am = 750
    per = 50
    print(p.discount_incurred(am, per))
