class Solution(object):

    def anagram(self, str1, str2):

        if sorted(str1.lower()) == sorted(str2.lower()):
            return True
        else:
            return False


if __name__ == "__main__":
    p = Solution()
    s1 = "cristian"
    s2 = "Cristina"
    t1 = "Nope"
    t2 = "Note"
    print(p.anagram(s1, s2))
    print(p.anagram(t1, t2))


