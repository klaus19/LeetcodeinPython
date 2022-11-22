class Solution(object):
    def kidwithCandies(self, candies, extraCandies):
        output = []
        max_candies = max(candies)

        for i in candies:
            if i + extraCandies > max_candies:
                output.append(True)
            else:
                output.append(False)

                return output



