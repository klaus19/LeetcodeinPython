class Solution(object):

    def count_consonants(self,s):

        to_char_array = set(s.lower())
        unique_list = list(to_char_array)

        conso = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        count_c = 0

        for item in range(len(unique_list)):

            if unique_list[item] not in conso:
                                      pass
            else:
                count_c = count_c+1
        return count_c

if __name__ == '__main__':
    s = "Count my unique consonants!!"
    t = "Dad"
    print(Solution().count_consonants(s))
    print(Solution().count_consonants(t))


