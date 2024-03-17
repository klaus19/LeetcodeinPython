from collections import Counter


class Solution(object):
    def removeDuplicateLetters(self, s):

        taken = set()
        count = Counter(s)
        st = []

        for char in s:
            if char not in taken:
                # check if there are any more instances of the evicting character
                while st and st[-1] > char and count[st[-1]] > 0:
                    taken.remove(st.pop())
                st.append(char)
                taken.add(char)
            count[char] -= 1  # finish processing this character
        return ''.join(st)

if __name__ == '__main__':
    s = "bcabc"
    print(Solution().removeDuplicateLetters(s))