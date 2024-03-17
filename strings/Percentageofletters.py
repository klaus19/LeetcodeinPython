class Solution(object):
    def percentageLetter(self, s, letter):
        list = [0] * 26
        for x in s:
            list[ord(x) - ord('a')] += 1
        occ = list[ord(letter) - ord('a')]
        return (occ * 100) // len(s)

if __name__ == '__main':
    s = "foobar"
    letter="o"

    print(Solution().percentageLetter(s, letter))