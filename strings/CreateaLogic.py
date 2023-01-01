class Solution(object):

    def findLogic(self, st):

        new_str = ''
        for i in range(0,len(st)):
            if st[i] == 'T':
                new_str += st[i]
            elif new_str == 'T' and st[i] == 'o':
                new_str += st[i]

            elif new_str == 'To' and st[i] == 'm':
                new_str += st[i]

            else:
                print("Tom cannot be found in the string")

        return new_str


if __name__ == "__main__":
    s = "Lord VoldemorT"
    p = 'Tajoekm'
    print(Solution().findLogic(s))
    print(Solution().findLogic(p))
