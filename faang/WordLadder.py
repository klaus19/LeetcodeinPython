from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> \
int:
        # Create a set of words for fast lookups
     word_set = set(wordList)
    # Edge case: if the endWord is not in the word_set, return 0
     if endWord not in word_set:
        return 0
    # Create a queue for the BFS and add the starting word
     queue = [(beginWord, 1)]
    # Create a set to keep track of visited words
     visited = set()
     while queue:
        # Dequeue the word
        word, length = queue.pop(0)
        # Check all possible transformations of the word
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + j + word[i+1:]
                if next_word == endWord:
                    return length + 1
                if next_word in word_set and next_word not in visited:
                    queue.append((next_word, length + 1))
                    visited.add(next_word)
     return 0