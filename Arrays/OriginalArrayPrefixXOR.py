class Solution(object):
    def findArray(self, pref):
        arr, n = [pref[0]], len(pref)
        for i in range(1, n):
            arr.append(pref[i - 1] ^ pref[i])
        return arr

if __name__ == '__main__':
    arr = [5,2,0,3,1]
    print(Solution().findArray(arr))