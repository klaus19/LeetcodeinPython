class Solution(object):

    def updation(self, list1, N, K):

        for i in range(0, len(list1)):
            if i == K:
                list1.insert(K,N)

        return list1


if __name__ == '__main__':
    ltr = [1, 2, 4, 5]
    list1 = [1, 1.23, "123"]
    k1=True
    k2=1
    Nt = 8
    Kt = 1
    print(Solution().updation(ltr, Nt, Kt))
    print(Solution().updation(list1,k1,k2))
