from collections import Counter


class Solution(object):

    def most_common(self,paragraph,ban):

        global find
        word_map = Counter(paragraph)

        for key,value in word_map.items():
            if key!=ban[0]:
                find = max(key)
            else:
                continue
        return find

if __name__ == '__main__':
    prara = "Bob hit a ball, the hit BALL flew far after it was hit."
    ban = ["hit"]
    print(Solution().most_common(prara,ban))