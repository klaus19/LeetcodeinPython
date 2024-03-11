from collections import Counter


class Solution(object):
    def minimumRounds(self, tasks) -> int:

        mapper = {}
        for task in tasks:
            mapper[task] = mapper.get(task,0)+1

        rounds = 0

        for count in mapper.values():
            if count == 1:
                return -1

            if count %3 ==0:
                rounds+=count//3

            else:
                rounds+=count//3+1

        return rounds

if __name__ == '__main__':
    arr =[2,2,3,3,2,4,4,4,4,4]
    print(Solution().minimumRounds(arr))