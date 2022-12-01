class Solution(object):

    def add_Two(self, no1, no2):
        n1 = int(no1)
        n2 = int(no2)

        if no1 == "" or no2 == "":
            return "Invalid Operation"
        else:
            return n1 + n2


if __name__ == "__main__":
    number1 = "100"
    number2 = "100"
    print(Solution().add_Two(number1, number2))
