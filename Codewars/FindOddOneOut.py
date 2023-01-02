class Solution(object):
    def find_it(self,nums):

        #using hashing and storing the occurances

        d = dict() #to store key:value pairs
        for i in nums:
            if i in d :
                d[i]+=1  #if element is present then increment its value by 1
            else:
                d[i]=1   #if element not present then initialize its value to 1

        for j in d.keys():
            if d[j]%2!=0:
                return j
            else:
                pass
        return j



if __name__ == "__main__":
    pt = [1,2,2,3,3,3,4,3,3,3,2,2,4]
    print(Solution().find_it(pt))

