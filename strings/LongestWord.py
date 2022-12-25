class Solution(object):

    def longest_word(self, words):
        curr_max = words[0]
        max_end = curr_max

        for i in range(1, len(words)):
            curr_max = max(max_end, words[i])
            max_end = curr_max

        return max_end


if __name__ == '__main__':
    pt = ["cat", "dog", "bird", "elephant"]
    print(Solution().longest_word(pt))
