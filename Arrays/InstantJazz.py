class Solution(object):
    def jazz(self, list=[]):

        for i in range(len(list)):
            if '7' not in list[i]:
                list[i]+'7'
            return list


if __name__ == "__main__":
    p = Solution()
    li = ['a', 'g', 'u']
    print(p.jazz(li))
