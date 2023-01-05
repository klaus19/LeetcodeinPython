class Solution(object):

    def in_array(self,array1, array2):
        arr = []
        for a2 in array2:
            for a1 in array1:
                if a1 in a2 and a1 not in arr:
                    arr.append(a1)
        return sorted(arr)
if __name__ == '__main__':
    pt1 =["tarp", "mice", "bull"]
    pt2 = ["lively", "alive", "harp", "sharp", "armstrong"]

    print(Solution().in_array(pt1,pt2))
