from collections import Counter


class Solution(object):

    def valueAns(self,ss):
        char_counts = Counter(ss)
        str1 = ""

        for char, count in char_counts.most_common():
            str1 += str(count) + char  # Append count first, then character

        return str1


if __name__ == '__main__':
    s = "WWMMWWCCC"
    print(Solution().valueAns(s))