class Solution(object):

    def to_binary(self, no):
        converted = bin(no)
        return converted


if __name__ == "__main__":
    n1 = 0xFF
    print(Solution().to_binary(n1))
