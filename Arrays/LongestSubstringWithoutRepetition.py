class Solution(object):

    def longest_substring(self,s):
        char_set = set()
        max_len = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                char_set.remove(s[i])
                i += 1
        return max_len

if __name__ == '__main__':
    st = 'abcabcbb'
    print(Solution().longest_substring(st))