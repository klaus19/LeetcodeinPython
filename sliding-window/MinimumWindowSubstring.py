
from collections import Counter
class Solution(object):

    def min_window_substring(self,s, t):
        if not s or not t:
            return ""

        target_counts = Counter(t)
        required_chars = len(target_counts)
        left = 0
        min_length = float('inf')
        result = ""

        for right, char in enumerate(s):
            if char in target_counts:
                target_counts[char] -= 1
                if target_counts[char] == 0:
                    required_chars -= 1

            while required_chars == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left:right + 1]

                if s[left] in target_counts:
                    target_counts[s[left]] += 1
                    if target_counts[s[left]] > 0:
                        required_chars += 1

                left += 1

        return result

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().min_window_substring(s,t))
