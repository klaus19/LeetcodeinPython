from collections import Counter


class Solution(object):

    def repeatedStrings(self,s,n):
        alpha_count = n // len(s)
        remaining_chars = n % len(s)

        full_string_count = alpha_count * Counter(s)['a']
        partial_string_count = Counter(s[:remaining_chars])['a']

        return full_string_count + partial_string_count

if __name__ == "__main__":
    st = "aba"
    n = 10
    print(Solution().repeatedStrings(st,n))

