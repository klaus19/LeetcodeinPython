from collections import Counter


class Solution(object):

    def frequencyChars(self, st):

        freq = Counter(st)

        sorted_chars = sorted(freq,key = freq.get,reverse = True)

        sorted_string = "".join([char*freq[char] for char in sorted_chars])

        return sorted_string




if __name__ == '__main__':
    st = "tree"
    print(Solution().frequencyChars(st))
