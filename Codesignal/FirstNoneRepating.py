class Solution(object):

    def nonrepeating(self, s):

        char_dict = {}
        res = []

        for idx, char in enumerate(s):
            countChar = 1 + char_dict.get(char, 0)
            char_dict[char] = countChar

        for idx, char in enumerate(s):
            if char_dict.get(char) == 1:
                res.append(char)

        if len(res) == 0:
            return -1
        else:
            return res[0]

if __name__ == "__main__":
    SS = "abacabad"
    print(Solution().nonrepeating(SS))

