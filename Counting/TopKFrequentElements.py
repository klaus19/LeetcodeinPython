from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):

        freq = Counter(nums)

        frequencies = list(freq.values())
        frequencies.sort(reverse=True)

        top_k_frequencies = frequencies[:k]

        result =[]
        for key,value in freq.items():
            if value in top_k_frequencies:
                result.append(key)

        return result

if __name__ == '__main__':
    arr  = [1,1,1,2,2,3]
    k =2
    print(Solution().topKFrequent(arr,k))
