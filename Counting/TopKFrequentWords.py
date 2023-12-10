from collections import Counter


class Solution(object):
    def topKFrequent(self, words, k):
        words.sort()
        freq = Counter(words).most_common(k)
        return list(map(lambda x: x[0], freq))

if __name__ == '__main__':
    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k=4
    print(Solution().topKFrequent(words,k))