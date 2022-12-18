class Solution(object):

    def addition(self, list1, list2):

        ltr = [*list1, *list2]

        new_lt=sorted(ltr)

        return new_lt


if __name__ == "__main__":
    lt1 = ["A", "E", "C"]
    lt2 = ["G", "F", "B"]

    print(Solution().addition(lt1, lt2))
