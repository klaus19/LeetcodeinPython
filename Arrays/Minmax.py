class Solution:

    def minmax(self, li):
        min_element = min(li)
        max_element = max(li)

        little = (min_element, max_element)
        return little


if __name__ == "__main__":
    p = Solution()
    troy = [1, 4, 2, 6, 7]
    print(p.minmax(troy))
