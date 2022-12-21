class Solution(object):

    def splitting_string(self, list1):  # Unsolved
        lesh = []
        fesh = []
        for word in range(0, len(list1)):
            l1 = list1[word].split()
            x = l1[0]
            y = l1[-1]

            lesh = lesh.append(x)
            fesh = fesh.append(y)

            final = [[*lesh], [*fesh]]

            return final


if __name__ == "__main__":
    lt = ["a A", "b B", "c C"]
    print(Solution().splitting_string(lt))
