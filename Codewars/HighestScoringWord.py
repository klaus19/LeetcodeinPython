class Solution(object):

    def highest_scoring_word(self, s):

        # Dictionary of English letters
        dt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
              'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
              'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
              'w': 23, 'x': 24, 'y': 25, 'z': 26}
        value_sum1 = 0
        max_value1 = value_sum1
        value_sum2 = 0
        max_value2 = value_sum2
        for i in range(0, len(s)):
            if s.upper():
                s = s.lower()
                words = s.split()

                # convert the string in char array
                to_char_array = list(words[0])

                j = 0
                while j < len(to_char_array):
                    if to_char_array[j] in dt.keys():
                        value_sum1 = max(dt.get(to_char_array[j]), value_sum1 + dt.get(to_char_array[j]))
                        max_value1 = max(value_sum1, max_value1)
                    else:
                        pass
                    j = j + 1

                to_char_array = list(words[1])

                j = 0
                while j < len(to_char_array):
                    if to_char_array[j] in dt.keys():
                        value_sum2 = max(dt.get(to_char_array[j]), value_sum2 + dt.get(to_char_array[j]))
                        max_value2 = max(value_sum2, max_value2)
                    else:
                        pass
                    j = j + 1
                if max_value2 > max_value1:
                    return max_value2
                elif max_value1 > max_value2:
                    return max_value1
                else:
                    return 'Both words have equal score'

        def high(self,x):
            return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

if __name__ == '__main__':
    p = 'abcd'
    print(Solution().highest_scoring_word(p))